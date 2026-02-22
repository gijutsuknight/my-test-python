# Relationship Extraction (REBEL)

Extract **(subject, relation, object)** triplets from text using the [REBEL](https://huggingface.co/Babelscape/rebel-large) model (Babelscape/rebel-large). No API key required; runs locally.

## Setup

1. Install dependencies (with venv active):
   ```bash
   pip install -r relationship-extraction/requirements.txt
   ```

2. On first run, the model will download from Hugging Face.

## Programs

### test.py — simplest test (inline text)

No config, no file. Text is defined in the script.

```bash
python relationship-extraction/test.py
```

### test-read-from-file.py — read from file + config

Reads input from a text file. Uses **read-from-file-config.yaml**:

- **input_file** — path to the .txt file (relative to this folder or absolute)
- **model** — Hugging Face model (default `Babelscape/rebel-large`)
- **max_length**, **num_beams**, **num_return_sequences** — generation options

Put your text in `input.txt` (or set `input_file` in the config), then:

```bash
python relationship-extraction/test-read-from-file.py
```

Output is a list of triplets: `(head, type, tail)` e.g. `(Steve Jobs, co-founded, Apple)`.
