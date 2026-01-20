from enum import Enum

class PIIEntity(str, Enum):
    """
    Enumeration of PII constants used in the system.
    Matches Presidio entity names where applicable.
    """
    PERSON = "PERSON"
    EMAIL_ADDRESS = "EMAIL_ADDRESS"
    PHONE_NUMBER = "PHONE_NUMBER"
    URL = "URL"
    LOCATION = "LOCATION"
    DATE_TIME = "DATE_TIME"
    
    # Financial / sensitive
    CREDIT_CARD = "CREDIT_CARD"
    IBAN_CODE = "IBAN_CODE"
    US_SSN = "US_SSN"
    US_DRIVER_LICENSE = "US_DRIVER_LICENSE"
    US_BANK_NUMBER = "US_BANK_NUMBER"
    US_PASSPORT = "US_PASSPORT"
    
    # Custom / Other
    POLISH_ID = "POLISH_ID"  # From original notebook
    TIME = "TIME"            # From original notebook
    UK_NHS = "UK_NHS"
    
    # Organization often useful for resumes
    ORGANIZATION = "ORGANIZATION"
