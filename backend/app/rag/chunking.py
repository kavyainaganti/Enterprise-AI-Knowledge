import re


def chunk_text(text: str, chunk_size: int = 900, overlap: int = 120) -> list[str]:
    """Character-based first-pass chunking with paragraph-aware boundaries.

    Values are characters, not tokens. This deliberately simple implementation
    will be upgraded to token-aware/section-aware chunking after ingestion tests.
    """
    if chunk_size <= overlap:
        raise ValueError("chunk_size must be greater than overlap")
    cleaned = re.sub(r"[ \t]+", " ", text.replace("\x00", " "))
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned).strip()
    if not cleaned:
        return []
    paragraphs = [p.strip() for p in cleaned.split("\n\n") if p.strip()]
    chunks, current = [], ""
    for paragraph in paragraphs:
        while len(paragraph) > chunk_size:
            if current:
                chunks.append(current)
                current = ""
            chunks.append(paragraph[:chunk_size])
            paragraph = paragraph[chunk_size - overlap:]
        candidate = f"{current}\n\n{paragraph}".strip() if current else paragraph
        if len(candidate) <= chunk_size:
            current = candidate
        else:
            if current:
                chunks.append(current)
            tail = current[-overlap:] if current else ""
            current = f"{tail}\n{paragraph}".strip() if tail else paragraph
            if len(current) > chunk_size:
                current = current[-chunk_size:]
    if current:
        chunks.append(current)
    return chunks
