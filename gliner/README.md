# GliNER (Zero-Shot NER)

Extract entities with **user-defined labels** at runtime — no training required.

## Setup

1. Install dependencies (with venv active):
   ```bash
   pip install -r gliner/requirements.txt
   ```

2. On first run, the model (`urchade/gliner_medium-v2.1`) will download from Hugging Face.

## Programs

### test.py — simplest test (inline text)

No config, no file. Text is defined in the script. Quick way to verify GliNER works.

```bash
python gliner/test.py
```

### test-read-from-file.py — read from file + config

Reads input from a text file. Uses **read-from-file-config.yaml** in this folder:

- **input_file** — path to the .txt file (relative to this folder or absolute)
- **model** — GliNER model name
- **threshold** — confidence threshold (0–1)
- **labels** — entity types to extract

Put your text in `input.txt` (or set `input_file` in the config), then:

```bash
python gliner/test-read-from-file.py
```

Optional: use a GPU for faster inference (install PyTorch with CUDA).
