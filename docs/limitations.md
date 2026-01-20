# Limitations

## Technical Limitations

### 1. NLP Accuracy
This system relies on Probabilistic Named Entity Recognition (NER). 
- **False Positives**: It might mark "Java" or "Python" as a `[LOCATION]` or `[NAME]` in rare contexts.
- **False Negatives**: It might miss meaningful names, especially if they are uncommon or appear in unusual contexts (e.g., headers without clear labels).

### 2. Context Sensitivity
The model works best with full sentences. Resume "bullet points" often lack grammatical structure, which can confuse the context-aware models of SpaCy.
- *Mitigation*: We use specific regex patterns for high-risk structured data like Emails and Phones to ensure they are caught even without context.

### 3. File Formats
Currently, the system only accepts **Text (.txt)** files.
- Resumes usually come in PDF or DOCX.
- **OCR Errors**: If you convert a PDF to text, OCR errors (e.g., "J0hn") will likely bypass the name detector.

### 4. Language Support
- **English Only**: The current configuration is tuned for English (`en` models). Using it on resumes in other languages will result in poor performance.

## Usage Limitations
- **Latency**: Processing large batches of resumes with the Large language model (`en_core_web_lg`) can be slow.
- **Memory**: The model requires significant RAM (~1GB+).
