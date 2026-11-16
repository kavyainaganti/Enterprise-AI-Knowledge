
import os

# Allow HTTP only for local development.
# Production deployments must use HTTPS.
if os.getenv("APP_ENV", "development") == "development":
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

from pathlib import Path
from typing import Any
import json

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

from app.core.config import settings


SCOPES = [
    "https://www.googleapis.com/auth/drive.readonly"
]


def _client_config() -> dict[str, Any]:
    if not settings.google_client_id or not settings.google_client_secret:
        raise RuntimeError(
            "Set GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET "
            "in backend/.env first."
        )

    return {
        "web": {
            "client_id": settings.google_client_id,
            "client_secret": settings.google_client_secret,
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "redirect_uris": [settings.google_redirect_uri],
        }
    }


def build_oauth_flow(state: str | None = None) -> Flow:
    """
    Create an OAuth flow for our confidential web application.

    PKCE generation is disabled for this local development
    implementation because the current callback does not
    persist the original code verifier between requests.
    """

    flow = Flow.from_client_config(
        _client_config(),
        scopes=SCOPES,
        state=state,
        autogenerate_code_verifier=False,
    )

    flow.redirect_uri = settings.google_redirect_uri

    return flow


def token_path() -> Path:
    path = settings.resolve_path(settings.google_token_file)
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


def save_credentials(credentials: Credentials) -> None:
    path = token_path()

    path.write_text(
        credentials.to_json(),
        encoding="utf-8",
    )


def load_credentials() -> Credentials:
    path = token_path()

    if not path.exists():
        raise RuntimeError(
            "Google Drive is not connected. "
            "Open /api/google-drive/auth-url first."
        )

    info = json.loads(
        path.read_text(encoding="utf-8")
    )

    credentials = Credentials.from_authorized_user_info(
        info,
        SCOPES,
    )

    if credentials.expired and credentials.refresh_token:
        from google.auth.transport.requests import Request

        credentials.refresh(Request())
        save_credentials(credentials)

    if not credentials.valid:
        raise RuntimeError(
            "Google Drive credentials are invalid. "
            "Reconnect Google Drive."
        )

    return credentials


def drive_service():
    credentials = load_credentials()

    return build(
        "drive",
        "v3",
        credentials=credentials,
        cache_discovery=False,
    )


def list_files(folder_id: str | None = None) -> list[dict]:
    folder_id = folder_id or settings.google_drive_folder_id

    if not folder_id:
        raise RuntimeError(
            "Set GOOGLE_DRIVE_FOLDER_ID or provide "
            "folder_id in the request."
        )

    service = drive_service()

    results = []
    page_token = None

    query = f"'{folder_id}' in parents and trashed = false"

    while True:
        response = service.files().list(
            q=query,
            pageSize=100,
            pageToken=page_token,
            fields=(
                "nextPageToken,"
                "files(id,name,mimeType,modifiedTime,size,webViewLink)"
            ),
            supportsAllDrives=True,
            includeItemsFromAllDrives=True,
        ).execute()

        results.extend(response.get("files", []))

        page_token = response.get("nextPageToken")

        if not page_token:
            return results


def download_file(
    file_id: str,
    name: str,
    mime_type: str,
    destination: Path,
) -> Path:

    service = drive_service()

    destination.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    google_exports = {
        "application/vnd.google-apps.document": (
            "application/pdf",
            ".pdf",
        ),
        "application/vnd.google-apps.spreadsheet": (
            "text/csv",
            ".csv",
        ),
        "application/vnd.google-apps.presentation": (
            "application/pdf",
            ".pdf",
        ),
    }

    if mime_type in google_exports:
        export_mime, extension = google_exports[mime_type]

        request = service.files().export_media(
            fileId=file_id,
            mimeType=export_mime,
        )

        destination = destination.with_suffix(extension)

    else:
        request = service.files().get_media(
            fileId=file_id,
            supportsAllDrives=True,
        )

    with destination.open("wb") as handle:
        downloader = MediaIoBaseDownload(
            handle,
            request,
        )

        done = False

        while not done:
            _, done = downloader.next_chunk()

    return destination
