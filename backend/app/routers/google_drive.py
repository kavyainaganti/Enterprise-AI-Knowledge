from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import RedirectResponse
from fastapi import Request
from uuid import uuid4
from app.services.google_drive import build_oauth_flow, save_credentials, list_files

router = APIRouter()
_pending_states: set[str] = set()

@router.get("/auth-url")
def google_auth_url():
    try:
        state = str(uuid4())
        flow = build_oauth_flow(state)
        url, _ = flow.authorization_url(
            access_type="offline", include_granted_scopes="true", prompt="consent"
        )
        _pending_states.add(state)
        return {"authorization_url": url, "message": "Open this URL and authorize read-only Drive access."}
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc))

@router.get("/callback")
def google_callback(request: Request, state: str = Query(...)):
    if state not in _pending_states:
        raise HTTPException(status_code=400, detail="Invalid or expired OAuth state. Start authorization again.")
    _pending_states.discard(state)
    try:
        flow = build_oauth_flow(state)
        flow.fetch_token(authorization_response=str(request.url))
        save_credentials(flow.credentials)
        return {"connected": True, "message": "Google Drive connected. You can now list files."}
    except Exception as exc:
        raise HTTPException(status_code=400, detail=f"Google OAuth failed: {exc}")

@router.get("/files")
def google_drive_files(folder_id: str | None = None):
    try:
        files = list_files(folder_id)
        return {"count": len(files), "files": files}
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc))
