from .pdf_extractor import extract_text as extract_pdf
from .docx_extractor import extract_text as extract_docx
from .base_extractor import BaseExtractor

__all__ = ["extract_pdf", "extract_docx", "BaseExtractor"]