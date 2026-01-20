from typing import List, Optional
from presidio_analyzer import AnalyzerEngine, RecognizerResult
from .config import AnonymizerConfig

class PIIDetector:
    """
    Wrapper around Presidio AnalyzerEngine to detect PII entities.
    """
    
    def __init__(self, language: str = AnonymizerConfig.DEFAULT_LANGUAGE):
        self.language = language
        self.analyzer = AnalyzerEngine()
        
        # Load custom recognizers
        custom_recognizers = AnonymizerConfig.get_custom_recognizers()
        for recognizer in custom_recognizers:
            self.analyzer.registry.add_recognizer(recognizer)
            
    def detect(self, text: str, entities: Optional[List[str]] = None) -> List[RecognizerResult]:
        """
        Detect PII in the given text.
        
        Args:
            text (str): Input text.
            entities (List[str], optional): List of entities to detect. If None, detects all.
            
        Returns:
            List[RecognizerResult]: Detected entities.
        """
        if not text:
            return []
            
        return self.analyzer.analyze(
            text=text,
            language=self.language,
            entities=entities
        )
