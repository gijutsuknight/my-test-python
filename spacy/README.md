# spaCy (Traditional NLP)

Test script for spaCy: tokenization, part-of-speech tagging, dependency parsing, named entity recognition, and lemmatization.

## Setup

1. Install dependencies from the spacy folder (with venv active):
   ```bash
   pip install -r spacy/requirements.txt
   ```

2. Download the small English model:
   ```bash
   python -m spacy download en_core_web_sm
   ```

## Run

```bash
python spacy/test.py
```
