# GliNER (Zero-Shot NER)

Test script for GliNER: extract entities with **user-defined labels** at runtime — no training required.

## Setup

1. Install dependencies (with venv active):
   ```bash
   pip install -r gliner/requirements.txt
   ```

2. On first run, the script will download the model (`urchade/gliner_medium-v2.1`) from Hugging Face.

## Run

```bash
python gliner/test.py
```

Optional: use a GPU for faster inference by installing PyTorch with CUDA and running the same command.
