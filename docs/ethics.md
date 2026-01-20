# Ethical Considerations

## Purpose: Reducing Bias
This tool is intended to aid in **Fair Hiring** practices. Research shows that unconscious bias against names, genders, ethnicities, and addresses can significantly affect hiring decisions. By stripping this information, we hope to allow candidates to be judged solely on their skills and experience.

## Privacy & Safety

### De-identification Risks
Anonymization is rarely perfect.
- **Linkability**: Even with names removed, a unique combination of "University", "Degree", "Graduation Year", and "Previous Employer" can uniquely identify an individual (k-anonymity violation).
- **Contextual PII**: "I am the son of the famous actor..." - NLP models may miss semantic PII that is not a named entity.

### Risk Mitigation
- **Human in the Loop**: This tool should be used as a *first pass*. A human reviewer should verify the output before sharing it widely.
- **Conservative Thresholds**: We rely on standard Presidio confidence scores. Lowering thresholds increases privacy but reduces utility (more false positives).

## Misuse
This tool should **not** be used to:
- "Clean" data for unauthorized sharing where strict GDPR/CCPA compliance is required without legal consultation.
- Automate adverse decisions without human oversight.

## Bias in the Anonymizer
The NLP models themselves (SpaCy/Presidio) may have biases. For example, they might be better at detecting Western names than non-Western names. This means a non-Western name might occasionally slip through (False Negative), unintentionally revealing the candidate's background. We mitigate this by using large, diverse models (`en_core_web_lg`), but the risk remains and users should be aware of it.
