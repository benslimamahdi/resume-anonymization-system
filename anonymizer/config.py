from presidio_analyzer import Pattern, PatternRecognizer

class AnonymizerConfig:
    """
    Configuration for the Anonymizer/Analyzer.
    """
    DEFAULT_LANGUAGE = "en"
    
    # Custom Patterns from the original notebook
    
    # Polish ID Pattern: 3 letters followed by 6 digits
    POLISH_ID_PATTERN = Pattern(
        name="polish_id_pattern",
        regex=r"[A-Z]{3}\d{6}",
        score=1.0,
    )
    
    # Time Pattern: HH:MM AM/PM
    TIME_PATTERN = Pattern(
        name="time_pattern",
        regex=r"(1[0-2]|0?[1-9]):[0-5][0-9] (AM|PM)",
        score=1.0,
    )
    
    @staticmethod
    def get_custom_recognizers():
        """
        Returns a list of custom recognizers to replace or augment default ones.
        """
        polish_id_recognizer = PatternRecognizer(
            supported_entity="POLISH_ID",
            patterns=[AnonymizerConfig.POLISH_ID_PATTERN]
        )
        
        time_recognizer = PatternRecognizer(
            supported_entity="TIME", 
            patterns=[AnonymizerConfig.TIME_PATTERN]
        )
        
        return [polish_id_recognizer, time_recognizer]
