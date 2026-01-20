# Evaluation Examples

## Sample 1: Standard Header
**Original**:
> John Doe
> 1234 Elm St, Springfield
> john.doe@example.com

**Anonymized**:
> [NAME]
> [LOCATION]
> [EMAIL]

## Sample 2: Contextual Mention
**Original**:
> "I worked closely with Jane Smith on the project."

**Anonymized**:
> "I worked closely with [NAME] on the project."

## Sample 3: False Positive (Potential)
**Original**:
> "Skilled in Amazon Web Services."

**Anonymized (Correct Behavior)**:
> "Skilled in [ORGANIZATION]." (If Organization is masked)
> *OR*
> "Skilled in Amazon Web Services." (If Organization is ignored)

*Note: In the current default config, Organization might be masked if detected as an entity.*
