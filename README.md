# Resume Anonymization System

A professional, open-source library and CLI tool for automatically detecting and anonymizing Personally Identifiable Information (PII) in resumes/CVs. 

> **Disclaimer**: This tool uses NLP models (Presidio/SpaCy) which are not 100% accurate. It is intended to assist in privacy preservation but should be supervised by human review for critical applications.

## 🚀 Features

- **Automated PII Detection**: Detects Name, Email, Phone, Location, URLs, Date/Time, and specific IDs (SSN, IBAN, etc.).
- **Smart Anonymization**: Replaces sensitive entities with standardized tokens (e.g., `[NAME]`, `[EMAIL]`) rather than simple masking, preserving document structure.
- **Configurable**: Easily extensibile with custom regex patterns and entities.
- **Privacy-First**: Designed for fair hiring pipelines to reduce unconscious bias.

## 📦 Installation

```bash
git clone https://github.com/yourusername/resume-anonymization.git
cd resume-anonymization
pip install -r requirements.txt
python -m spacy download en_core_web_lg
```

## 🛠 Usage

### Command Line Interface

To anonymize a single resume:

```bash
python inference/anonymize_resume.py --input data/raw/sample_resume.txt --output data/anonymized/sample_resume_anonymized.txt
```

### Python API

```python
from anonymizer.detector import PIIDetector
from anonymizer.anonymizer import PIIAnonymizer

text = "Contact John Doe at john@example.com"

# 1. Detect
detector = PIIDetector()
results = detector.detect(text)

# 2. Anonymize
anonymizer = PIIAnonymizer()
anonymized_text = anonymizer.anonymize(text, results)

print(anonymized_text)
# Output: "Contact [NAME] at [EMAIL]"
```

## 📂 Project Structure

- `anonymizer/`: Core logic for detection and anonymization.
- `notebooks/`: Exploratory notebooks (e.g., experimental Presidio logic).
- `inference/`: Scripts for running the anonymizer on files.
- `data/`: Sample data handling (includes synthetic examples only).
- `docs/`: Detailed architectural and ethical documentation.

## 🛡 Ethical Considerations

This project is built to support **fair hiring** practices. By removing demographic markers (Names, Locations, etc.) from resumes before review, organizations can reduce unconscious bias. However, privacy engineering is complex. Please read [docs/ethics.md](docs/ethics.md) for a deep dive into the risks and limitations.

## ⚠️ Limitations

- **False Positives/Negatives**: No NLP model is perfect. Context is sometimes missed.
- **Multilingual Support**: Currently optimized for English.
- **Format Support**: Supports plain text extracts. PDFs/Word docs must be converted to text first.

See [docs/limitations.md](docs/limitations.md) for more details.

## 📄 License

Apache License 2.0 - see [LICENSE](LICENSE) for details.
