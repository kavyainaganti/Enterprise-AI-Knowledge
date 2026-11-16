from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

BACKEND_DIR = Path(__file__).resolve().parents[2]

class Settings(BaseSettings):
    app_env: str = "development"
    frontend_origin: str = "http://localhost:5173"
    google_client_id: str = ""
    google_client_secret: str = ""
    google_redirect_uri: str = "http://localhost:8000/api/google-drive/callback"
    google_drive_folder_id: str = ""
    google_token_file: str = "backend/data/google_token.json"
    qdrant_url: str = ""
    qdrant_api_key: str = ""
    qdrant_collection: str = "enterprise_knowledge"
    qdrant_local_path: str = "backend/data/qdrant"
    embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2"
    groq_api_key: str = ""
    groq_model: str = "llama-3.3-70b-versatile"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    def resolve_path(self, value: str) -> Path:
        path = Path(value)
        return path if path.is_absolute() else (BACKEND_DIR.parent / path).resolve()

settings = Settings()
