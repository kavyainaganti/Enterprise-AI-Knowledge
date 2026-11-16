from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.routers import documents, chat, google_drive

app = FastAPI(
    title="Enterprise AI Knowledge and Decision Platform API",
    description="Backend services for Google Drive ingestion, Qdrant retrieval and enterprise knowledge chat.",
    version="0.2.0",
)

origins = [settings.frontend_origin]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["Authorization", "Content-Type"],
)

app.include_router(google_drive.router, prefix="/api/google-drive", tags=["Google Drive"])
app.include_router(documents.router, prefix="/api/documents", tags=["Documents"])
app.include_router(chat.router, prefix="/api/chat", tags=["RAG Chat"])

@app.get("/")
def root():
    return {"message": "Enterprise AI Knowledge Platform backend", "docs": "/docs"}

@app.get("/api/health")
def health():
    return {"status": "healthy", "service": "enterprise-ai-backend", "version": app.version}
