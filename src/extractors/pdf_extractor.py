import PyPDF2
from .base_extractor import BaseExtractor

class PDFExtractor(BaseExtractor):
    def extract_text(self, uploaded_file) -> str:
        """
        Extracts text from a Streamlit UploadedFile object.
        """
        try:
            # Streamlit files act as file-like objects, so PyPDF2 can read them directly
            reader = PyPDF2.PdfReader(uploaded_file)
            text = ""
            
            for page in reader.pages:
                extracted = page.extract_text()
                if extracted:
                    text += extracted + "\n"
                    
            if not text.strip():
                raise ValueError("No text found. Is this a scanned image?")
                
            return text.strip()
            
        except Exception as e:
            # This catches corruption, password protection, or empty files
            raise Exception(f"Failed to parse PDF: {str(e)}")

# If you are using functions instead of classes in your __init__.py mapping:
def extract_text(uploaded_file) -> str:
    extractor = PDFExtractor()
    return extractor.extract_text(uploaded_file)