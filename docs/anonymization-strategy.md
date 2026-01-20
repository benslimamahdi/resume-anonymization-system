# Anonymization Strategy

## Philosophy
The goal of this system is to remove bias-inducing information while retaining the professional content of a resume. We prioritize **safety** (removing all potential PII) over **readability** where conflicts arise, although we strive for both.

## Method: Token Replacement
We use **Token Replacement** rather than redaction (blacking out) or synthetic replacement (fake names).

### Why Token Replacement?
1. **Context Preservation**: Changing "John Doe" to `[NAME]` usually keeps the sentence grammatical structure intact, unlike redaction which might leave gaps.
2. **Clarity**: It is immediately obvious to the human reviewer that information has been removed. Synthetic data (replacing "John" with "Steve") can be confusing if the reviewer tries to look up "Steve".
3. **Machine Parsability**: Downstream systems can easily identify that `[EMAIL]` is a placeholder.

## Comparison of Methods

| Method | Example Input | Example Output | Pros | Cons |
|--------|---------------|----------------|------|------|
| **Token Replacement** (Selected) | "Call John" | "Call [NAME]" | Clear, Safe | Loses flow |
| **Masking** | "Call John" | "Call ****" | Safe | Hard to read |
| **Synthetic/Faker** | "Call John" | "Call Steve" | Readable | Misleading |

## Entities Handled

| Entity | Token | Description |
|--------|-------|-------------|
| PERSON | `[NAME]` | Names of people |
| EMAIL_ADDRESS | `[EMAIL]` | Email addresses |
| PHONE_NUMBER | `[PHONE]` | Phone numbers |
| URL | `[URL]` | Websites, LinkedIn profiles |
| LOCATION | `[LOCATION]` | Cities, Addresses |
| DATE_TIME | `[DATE]` / `[TIME]` | Dates (DOB, etc.) |
| ORGANIZATION | `[ORGANIZATION]` | Company names (Optional/Context dependent) |
| ID Numbers | `[SSN]`, `[ID]` | Government IDs |

## Configurability
The mapping of Entities to Tokens is defined in `anonymizer/anonymizer.py` and can be customized.
