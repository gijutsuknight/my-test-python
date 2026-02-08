# LLM-Based Entity Extraction (LangChain)

Test script for entity extraction using LangChain and OpenAI: extract entities with **types** and **descriptions** via a single prompt.

## Setup

1. Install dependencies (with venv active):
   ```bash
   pip install -r llm-based-extraction/requirements.txt
   ```

2. Set your OpenAI API key. Copy or edit `.env` in this folder (`llm-based-extraction/.env`):
   ```
   OPENAI_API_KEY=your-api-key-here
   ```
   The script loads it automatically. Do not commit real keys (`.env` is in `.gitignore`).

## Run

```bash
python llm-based-extraction/test.py
```

The script uses `gpt-4o` by default. Change the model in `test.py` if needed (e.g. `gpt-4o-mini` for lower cost).
