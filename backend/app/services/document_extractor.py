from pathlib import Path
import fitz
from docx import Document
from pptx import Presentation
from openpyxl import load_workbook

SUPPORTED_EXTENSIONS = {".pdf", ".docx", ".txt", ".pptx", ".xlsx", ".csv"}


def extract_document(path: Path) -> list[dict]:
    ext = path.suffix.lower()
    pages: list[dict] = []
    if ext == ".pdf":
        with fitz.open(path) as pdf:
            for i, page in enumerate(pdf):
                text = page.get_text("text").strip()
                if text:
                    pages.append({"page_number": i + 1, "text": text})
    elif ext == ".docx":
        doc = Document(path)
        text = "\n".join(p.text for p in doc.paragraphs if p.text.strip())
        for table in doc.tables:
            text += "\n" + "\n".join(" | ".join(c.text for c in row.cells) for row in table.rows)
        if text.strip(): pages.append({"page_number": None, "text": text.strip()})
    elif ext == ".txt":
        text = path.read_text(encoding="utf-8", errors="ignore").strip()
        if text: pages.append({"page_number": None, "text": text})
    elif ext == ".pptx":
        prs = Presentation(path)
        for i, slide in enumerate(prs.slides):
            text = "\n".join(shape.text for shape in slide.shapes if hasattr(shape, "text") and shape.text.strip())
            if text.strip(): pages.append({"page_number": i + 1, "text": text})
    elif ext == ".xlsx":
        wb = load_workbook(path, read_only=True, data_only=True)
        for sheet in wb.worksheets:
            rows = []
            for row in sheet.iter_rows(values_only=True):
                values = [str(v) for v in row if v is not None]
                if values: rows.append(" | ".join(values))
            if rows: pages.append({"page_number": None, "text": f"Sheet: {sheet.title}\n" + "\n".join(rows)})
    elif ext == ".csv":
        text = path.read_text(encoding="utf-8-sig", errors="ignore").strip()
        if text: pages.append({"page_number": None, "text": text})
    else:
        raise ValueError(f"Unsupported document format: {ext}")
    return pages
