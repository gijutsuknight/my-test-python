# LLM-Based Entity Extraction (LangChain)

Extract entities with **types** and **descriptions** using LangChain and OpenAI.

## Setup

1. Install dependencies (with venv active):
   ```bash
   pip install -r llm-based-extraction/requirements.txt
   ```

2. Set API key(s) in `.env` in this folder:
   - **OpenAI:** `OPENAI_API_KEY=...` ([platform.openai.com](https://platform.openai.com/api-keys))
   - **Gemini:** `GOOGLE_API_KEY=...` ([aistudio.google.com/apikey](https://aistudio.google.com/apikey))
   Scripts load them automatically. Do not commit real keys (`.env` is in `.gitignore`).

## Programs

### test.py — simplest test (inline text)

No config, no file. Text is defined in the script. Uses OpenAI by default. To use Gemini:

```bash
LLM_PROVIDER=gemini python llm-based-extraction/test.py
```

Optional: `LLM_MODEL=gemini-2.0-flash` or `gpt-4o-mini` to override the model.

### test-read-from-file.py — read from file + config

Reads input from a text file. Uses **read-from-file-config.yaml**:

- **input_file** — path to the .txt file (relative to this folder or absolute)
- **provider** — `openai` or `gemini`
- **model** — e.g. `gpt-4o`, `gpt-4o-mini`, or `gemini-2.0-flash` (when using Gemini)
- **temperature** — 0 for deterministic output

Set `provider: "gemini"` and `model: "gemini-2.0-flash"` in the config to use Google Gemini (requires `GOOGLE_API_KEY` in `.env`). Then:

```bash
python llm-based-extraction/test-read-from-file.py
```
