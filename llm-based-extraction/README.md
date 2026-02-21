# LLM-Based Entity Extraction (LangChain)

Extract entities with **types** and **descriptions** using LangChain and OpenAI.

## Setup

1. Install dependencies (with venv active):
   ```bash
   pip install -r llm-based-extraction/requirements.txt
   ```

2. Set your OpenAI API key. Copy or edit `.env` in this folder (`llm-based-extraction/.env`):
   ```
   OPENAI_API_KEY=your-api-key-here
   ```
   The scripts load it automatically. Do not commit real keys (`.env` is in `.gitignore`).

## Programs

### test.py — simplest test (inline text)

No config, no file. Text is defined in the script.

```bash
python llm-based-extraction/test.py
```

### test-read-from-file.py — read from file + config

Reads input from a text file. Uses **read-from-file-config.yaml** in this folder:

- **input_file** — path to the .txt file (relative to this folder or absolute)
- **model** — OpenAI model (e.g. `gpt-4o`, `gpt-4o-mini`)
- **temperature** — 0 for deterministic output

Put your text in `input.txt` (or set `input_file` in the config), then:

```bash
python llm-based-extraction/test-read-from-file.py
```
