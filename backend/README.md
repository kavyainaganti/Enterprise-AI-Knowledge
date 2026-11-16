# Enterprise AI Knowledge and Decision Platform — Backend

This backend is added to the existing `novatech-frontend` project. It uses FastAPI, Google Drive API, Sentence Transformers and **Qdrant**.

## Current implementation stage

Implemented in this starter continuation:

- FastAPI application and health endpoint.
- Google Drive OAuth URL/callback and folder file listing.
- Download/export of supported Drive files (PDF, DOCX, TXT, XLSX, CSV, PPTX and Google Docs/Sheets/Slides exports).
- Text extraction, first-pass paragraph chunking and Sentence Transformers embeddings.
- Qdrant storage (persistent local mode by default, or hosted Qdrant using `QDRANT_URL`).
- Semantic retrieval endpoint through the chat route.
- Optional Groq answer generation when `GROQ_API_KEY` is configured.
- React ChatBox changed to call the FastAPI chat endpoint instead of its hardcoded mock answer rules.

Not implemented yet: production authentication/JWT, verified backend RBAC, department/role permission enforcement, audit persistence, OCR for scanned PDFs, incremental Drive sync, document deletion/update reconciliation, decision advisor and workflow assistant. The current Google OAuth state is held in process memory for local development only.

**Security warning:** Do not expose this development backend to employees or ingest confidential production documents yet. The current chat and ingestion routes do not enforce authenticated user identity or document-level RBAC. `allowed_roles` is stored as metadata only at this stage; it is not an access-control boundary. Implement and test JWT + server-side Qdrant metadata filters before production use.

## 1. Requirements

- Python 3.11 recommended.
- Node.js compatible with the existing Vite project.
- A Google Cloud project with Google Drive API enabled and OAuth 2.0 Web application credentials.
- A Google Drive folder ID.
- Optional Groq API key for answer generation. Retrieval works without it.

## 2. Backend setup on Windows PowerShell

Open a terminal in the `novatech-frontend` project root:

```powershell
cd backend
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
```

Edit `backend/.env` and fill in Google OAuth values. For local testing, set:

```env
FRONTEND_ORIGIN=http://localhost:5173
GOOGLE_REDIRECT_URI=http://localhost:8000/api/google-drive/callback
GOOGLE_DRIVE_FOLDER_ID=YOUR_FOLDER_ID
QDRANT_COLLECTION=enterprise_knowledge
QDRANT_LOCAL_PATH=backend/data/qdrant
EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

Create an OAuth 2.0 Client ID of type **Web application** in Google Cloud Console. Add this exact Authorized redirect URI:

`http://localhost:8000/api/google-drive/callback`

Enable Google Drive API. The app requests read-only Drive scope. Store the client secret only in `backend/.env`; never put it in the Vite frontend environment or commit it.

## 3. Start the backend

From the `backend` directory, with `.venv` activated:

```powershell
uvicorn app.main:app --reload
```

Open:

- http://127.0.0.1:8000/api/health
- http://127.0.0.1:8000/docs

## 4. Connect Google Drive

1. Open `http://127.0.0.1:8000/api/google-drive/auth-url`.
2. Copy the returned `authorization_url` into your browser.
3. Sign in to the Google account that can read the source folder and grant read-only access.
4. The callback saves a refresh token to `backend/data/google_token.json`.
5. Open `http://127.0.0.1:8000/api/google-drive/files` to list the configured folder's files.

The OAuth token file is private and gitignored. For deployment, replace the local token-file approach with encrypted secret storage and a durable, session-bound OAuth state mechanism.

## 5. Ingest a Drive folder

Use Swagger UI at `http://127.0.0.1:8000/docs` and call `POST /api/documents/ingest-drive` with:

```json
{
  "folder_id": "YOUR_GOOGLE_DRIVE_FOLDER_ID",
  "department": "Unclassified",
  "allowed_roles": []
}
```

For the first test, use a folder containing non-confidential sample documents. The embedding model downloads on first use and may take time. Qdrant local storage is created under `backend/data/qdrant`.

Scanned/image-only PDFs are reported as having no extractable text; OCR is a later implementation stage.

## 6. Connect the React frontend

In the project root (`novatech-frontend`), create `.env` from `.env.example`:

```env
VITE_API_BASE_URL=http://127.0.0.1:8000
```

Install frontend packages if needed and start Vite in a second terminal:

```powershell
npm install
npm run dev
```

The existing `src/components/ChatBox.jsx` now calls `POST /api/chat`. After successful ingestion, ask a question that is answered by one of the indexed documents.

## 7. Optional Groq generation

Set `GROQ_API_KEY` in `backend/.env`. The backend calls Groq's OpenAI-compatible chat completions endpoint and supplies retrieved document chunks as context. The prompt instructs the model not to invent facts outside the retrieved context.

Without a Groq key, the chat endpoint returns a retrieval status and source citations so you can test Qdrant independently.

## 8. Qdrant deployment choices

- Local development: leave `QDRANT_URL` empty; Qdrant client uses persistent local storage.
- Hosted Qdrant: set `QDRANT_URL` and `QDRANT_API_KEY` to your Qdrant cluster credentials. Do not set a local path for hosted mode.

The configured embedding model produces 384-dimensional vectors. If you change embedding models, create a new Qdrant collection with the matching vector size or rebuild the collection; vectors from different models must not be mixed.
