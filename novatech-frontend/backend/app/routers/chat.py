import httpx
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from app.core.config import settings
from app.rag.retrieval import retrieve_relevant_chunks

router = APIRouter()

class ChatRequest(BaseModel):
    question: str = Field(min_length=2, max_length=4000)
    top_k: int = Field(default=5, ge=1, le=10)

@router.post("")
async def chat(request: ChatRequest):
    try:
        matches = retrieve_relevant_chunks(request.question, request.top_k)
    except Exception as exc:
        raise HTTPException(status_code=503, detail=f"RAG retrieval is not ready: {exc}")

    if not matches:
        return {
            "answer": "I could not find relevant information in the indexed enterprise documents. Please check whether the correct Google Drive folder has been ingested.",
            "sources": [],
            "retrieved_chunks": 0,
        }

    context_parts, sources = [], []
    for item in matches:
        context_parts.append(
            f"[Document: {item.get('filename')} | Page: {item.get('page_number') or 'N/A'}]\n{item.get('text', '')}"
        )
        source = {
            "document": item.get("filename", "Unknown document"),
            "page": item.get("page_number"),
            "url": item.get("source_url", ""),
            "score": round(float(item.get("score", 0)), 4),
        }
        if source not in sources:
            sources.append(source)

    context = "\n\n---\n\n".join(context_parts)
    if not settings.groq_api_key:
        answer = "Relevant document passages were retrieved successfully. Configure GROQ_API_KEY in backend/.env to enable grounded natural-language answer generation."
        return {"answer": answer, "sources": sources, "retrieved_chunks": len(matches), "context_preview": context[:5000]}

    prompt = (
        "You are the Enterprise AI Knowledge Assistant. Answer only using the supplied context. "
        "If the context does not contain the answer, say that the available documents do not specify it. "
        "Do not invent policies, numbers, eligibility rules or procedures. Be concise.\n\n"
        f"CONTEXT:\n{context}\n\nQUESTION:\n{request.question}"
    )
    try:
        async with httpx.AsyncClient(timeout=45) as client:
            response = await client.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers={"Authorization": f"Bearer {settings.groq_api_key}", "Content-Type": "application/json"},
                json={"model": settings.groq_model, "messages": [{"role": "user", "content": prompt}], "temperature": 0.1},
            )
            response.raise_for_status()
            answer = response.json()["choices"][0]["message"]["content"]
    except Exception as exc:
        raise HTTPException(status_code=502, detail=f"LLM generation failed: {exc}")

    return {"answer": answer, "sources": sources, "retrieved_chunks": len(matches)}
