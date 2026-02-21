"""
LLM-based entity extraction: read input text from a file.
Uses its own config (read-from-file-config.yaml). Supports OpenAI or Gemini via .env keys.
"""
import json
import os
import re
from pathlib import Path

from dotenv import load_dotenv
import yaml
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI

SCRIPT_DIR = Path(__file__).resolve().parent
CONFIG_FILE = SCRIPT_DIR / "read-from-file-config.yaml"

load_dotenv(SCRIPT_DIR / ".env")

EXTRACTION_PROMPT = """
Extract all entities from the following text. For each entity, provide:
- entity_name: The name of the entity
- entity_type: The type (Project, Task, User, etc.)
- description: A brief description based on context

Text: {text}

Return as JSON array.
"""


def load_config() -> dict:
    if not CONFIG_FILE.exists():
        raise FileNotFoundError(f"Config not found: {CONFIG_FILE}")
    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def get_llm(provider: str, model: str, temperature: float):
    """Return OpenAI or Gemini chat model from config."""
    provider = (provider or "openai").strip().lower()
    if provider == "gemini":
        if not os.environ.get("GOOGLE_API_KEY"):
            raise ValueError("Set GOOGLE_API_KEY in .env to use Gemini (https://aistudio.google.com/apikey)")
        return ChatGoogleGenerativeAI(model=model or "gemini-2.0-flash", temperature=temperature)
    return ChatOpenAI(model=model or "gpt-4o", temperature=temperature)


def main() -> None:
    config = load_config()
    input_file = Path(config.get("input_file", "input.txt"))
    if not input_file.is_absolute():
        input_file = SCRIPT_DIR / input_file
    if not input_file.exists():
        raise FileNotFoundError(f"Input file not found: {input_file}")

    provider = config.get("provider", "openai")
    model_name = config.get("model") or ("gpt-4o" if provider == "openai" else "gemini-2.0-flash")
    temperature = float(config.get("temperature", 0))

    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()

    llm = get_llm(provider, model_name, temperature)
    prompt = PromptTemplate.from_template(EXTRACTION_PROMPT)
    chain = prompt | llm

    response = chain.invoke({"text": text})
    content = response.content.strip()

    json_match = re.search(r"```(?:json)?\s*([\s\S]*?)```", content)
    if json_match:
        content = json_match.group(1).strip()
    raw = content

    try:
        entities = json.loads(content)
    except json.JSONDecodeError:
        entities = []
        print("Raw response (JSON parse failed):\n", raw[:500])

    print("=== LLM-based entity extraction (from file) ===\n")
    for e in entities:
        name = e.get("entity_name", "")
        etype = e.get("entity_type", "")
        desc = e.get("description", "")
        print(f"  {name} ({etype})")
        if desc:
            print(f"    → {desc}")
        print()


if __name__ == "__main__":
    main()
