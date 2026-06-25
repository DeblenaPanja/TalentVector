import docx

def extract_text(file) -> str:
    """Extracts raw text from a Streamlit uploaded DOCX file object."""
    try:
        doc = docx.Document(file)
        full_text = [para.text for para in doc.paragraphs]
        return "\n".join(full_text).strip()
    except Exception as e:
        return f"Error parsing DOCX: {str(e)}"