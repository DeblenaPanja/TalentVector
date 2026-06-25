from abc import ABC, abstractmethod

class BaseExtractor(ABC):
    """
    Abstract base class for all file extractors.
    Any new extractor (e.g., ImageExtractor) must implement the 'extract_text' method.
    """
    
    @abstractmethod
    def extract_text(self, file) -> str:
        """Must return a string of text from the file."""
        pass