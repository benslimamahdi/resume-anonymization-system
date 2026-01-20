import argparse
import sys
import os
from pathlib import Path

# Ensure the project root is in sys.path to allow imports from anonymizer
current_dir = Path(__file__).resolve().parent
project_root = current_dir.parent
sys.path.append(str(project_root))

from anonymizer.detector import PIIDetector
from anonymizer.anonymizer import PIIAnonymizer

def main():
    parser = argparse.ArgumentParser(description="Anonymize PII in a resume text file.")
    parser.add_argument("--input", "-i", type=str, required=True, help="Path to the input resume file (txt).")
    parser.add_argument("--output", "-o", type=str, required=True, help="Path to save the anonymized output.")
    
    args = parser.parse_args()
    
    input_path = Path(args.input)
    output_path = Path(args.output)
    
    if not input_path.exists():
        print(f"Error: Input file '{input_path}' not found.")
        sys.exit(1)
        
    print(f"Reading from {input_path}...")
    try:
        with open(input_path, "r", encoding="utf-8") as f:
            text = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)
        
    print("Initializing detector and anonymizer...")
    detector = PIIDetector()
    anonymizer = PIIAnonymizer()
    
    print("Detecting PII...")
    analyzer_results = detector.detect(text)
    print(f"Found {len(analyzer_results)} PII entities.")
    for res in analyzer_results:
        print(f" - Found {res.entity_type} at {res.start}:{res.end} (Score: {res.score})")
        
    print("Anonymizing...")
    anonymized_text = anonymizer.anonymize(text, analyzer_results)
    
    print(f"Writing output to {output_path}...")
    try:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(anonymized_text)
    except Exception as e:
        print(f"Error writing file: {e}")
        sys.exit(1)
        
    print("Done!")

if __name__ == "__main__":
    main()
