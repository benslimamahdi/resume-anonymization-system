from typing import List, Dict, Any
from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import OperatorConfig, RecognizerResult
from presidio_anonymizer.entities import EngineResult
from .entities import PIIEntity

class PIIAnonymizer:
    """
    Wrapper around Presidio AnonymizerEngine to mask PII entities.
    """
    
    # Mapping from Presidio/Custom Entities to display tokens
    # Per instructions: [NAME], [EMAIL], [PHONE] etc.
    TOKEN_MAPPING = {
        PIIEntity.PERSON: "[NAME]",
        PIIEntity.EMAIL_ADDRESS: "[EMAIL]",
        PIIEntity.PHONE_NUMBER: "[PHONE]",
        PIIEntity.URL: "[URL]",
        PIIEntity.LOCATION: "[LOCATION]",
        PIIEntity.DATE_TIME: "[DATE]",
        PIIEntity.TIME: "[TIME]",
        PIIEntity.POLISH_ID: "[POLISH_ID]",
        PIIEntity.CREDIT_CARD: "[CREDIT_CARD]",
        PIIEntity.IBAN_CODE: "[IBAN]",
        PIIEntity.US_SSN: "[SSN]",
        PIIEntity.US_DRIVER_LICENSE: "[DRIVER_LICENSE]",
        PIIEntity.US_BANK_NUMBER: "[BANK_NUMBER]",
        PIIEntity.US_PASSPORT: "[PASSPORT]",
        PIIEntity.UK_NHS: "[NHS_NUMBER]",
        PIIEntity.ORGANIZATION: "[ORGANIZATION]",
    }

    def __init__(self):
        self.engine = AnonymizerEngine()

    def anonymize(self, text: str, analyzer_results: List[RecognizerResult]) -> str:
        """
        Anonymize the text using the provided analyzer results.
        
        Args:
            text (str): Input text.
            analyzer_results (List[RecognizerResult]): Detection results.
            
        Returns:
            str: Anonymized text.
        """
        if not text:
            return ""

        # Define operators for each entity found
        # We use a custom 'replace' operator to map to our specific tokens
        operators: Dict[str, OperatorConfig] = {}
        
        # We assume that for any entity we want to replace it with its mapped token
        # If an entity is not in our map, we default to standard Presidio behavior (usually hash or just <ENTITY>)
        # But to be safe and uniform, we will fallback to brackets
        
        for entity_type in self.TOKEN_MAPPING.keys():
            token = self.TOKEN_MAPPING.get(entity_type, f"[{entity_type}]")
            operators[entity_type] = OperatorConfig("replace", {"new_value": token})

        # Run anonymization
        result = self.engine.anonymize(
            text=text,
            analyzer_results=analyzer_results,
            operators=operators
        )
        
        return result.text
