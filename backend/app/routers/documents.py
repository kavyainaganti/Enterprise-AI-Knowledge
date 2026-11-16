from pathlib import Path
import re
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.core.config import settings
from app.services.google_drive import list_files, download_file
from app.services.document_extractor import extract_document, SUPPORTED_EXTENSIONS
from app.rag.chunking import chunk_text
from app.rag.embeddings import embed_texts
from app.rag.vector_store import upsert_chunks

router = APIRouter()

class IngestRequest(BaseModel):
    folder_id: str | None = None
    department: str = "Unclassified"
    allowed_roles: list[str] = []

@router.post("/ingest-drive")
def ingest_drive_folder(request: IngestRequest):
    """Download, extract, chunk, embed and index supported files from one Drive folder.

    Development milestone only: access roles are stored as metadata but are not
    yet enforced at retrieval time. Do not expose this API to employees until JWT/RBAC is added.
    """
    try:
        files = list_files(request.folder_id)
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc))

    root = settings.resolve_path("backend/data/documents")
    root.mkdir(parents=True, exist_ok=True)
    indexed, skipped, errors = [], [], []

    for file in files:
        name = file.get("name", "document")
        mime = file.get("mimeType", "")
        suffix = Path(name).suffix.lower()
        google_native = mime in {
            "application/vnd.google-apps.document",
            "application/vnd.google-apps.spreadsheet",
            "application/vnd.google-apps.presentation",
        }
        if suffix not in SUPPORTED_EXTENSIONS and not google_native:
            skipped.append({"name": name, "reason": "Unsupported file type"})
            continue
        try:
            safe_name = re.sub(r"[^A-Za-z0-9._-]", "_", name)[:140]
            local_path = root / f"{file['id']}_{safe_name}"
            local_path = download_file(file["id"], name, mime, local_path)
            pages = extract_document(local_path)
            if not pages:
                skipped.append({"name": name, "reason": "No extractable text; scanned PDFs need OCR"})
                continue
            docs_to_embed, payloads = [], []
            for page in pages:
                for index, chunk in enumerate(chunk_text(page["text"])):
                    docs_to_embed.append(chunk)
                    payloads.append({
                        "chunk_id": f"{file['id']}:p{page['page_number'] or 0}:c{index}",
                        "text": chunk,
                        "document_id": file["id"],
                        "filename": name,
                        "mime_type": mime,
                        "page_number": page["page_number"],
                        "department": request.department,
                        "allowed_roles": request.allowed_roles,
                        "source_url": file.get("webViewLink", ""),
                    })
            vectors = embed_texts(docs_to_embed)
            for payload, vector in zip(payloads, vectors):
                payload["embedding"] = vector
            count = upsert_chunks(payloads)
            indexed.append({"name": name, "document_id": file["id"], "chunks_indexed": count})
        except Exception as exc:
            errors.append({"name": name, "error": str(exc)})

    return {
        "indexed_count": len(indexed),
        "skipped_count": len(skipped),
        "error_count": len(errors),
        "indexed": indexed,
        "skipped": skipped,
        "errors": errors,
        "warning": "RBAC filtering is not implemented yet. Do not use this development endpoint with confidential documents or expose chat to employees until backend authentication and permission filtering are added."
    }
