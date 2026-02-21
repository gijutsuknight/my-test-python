"""
LLM-based entity extraction: read input text from a file.
Uses its own config (read-from-file-config.yaml). Loads OPENAI_API_KEY from .env.
"""
import json
import re
from pathlib import Path

from dotenv import load_dotenv
import yaml
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

SCRIPT_DIR = Path(__file__).resolve().parent
CONFIG_FILE = SCRIPT_DIR / "read-from-file-config.yaml"

load_dotenv(SCRIPT_DIR / ".env")

EXTRACTION_PROMPT = """
Extract all entities from the following text. For each entity, provide:
- entity_name: The name of the entity
- entity_type: The type (PERSON, ORG, PRODUCT, CONCEPT, etc.)
- description: A brief description based on context

Text: {text}

Return as JSON array.
"""


def load_config() -> dict:
    if not CONFIG_FILE.exists():
        raise FileNotFoundError(f"Config not found: {CONFIG_FILE}")
    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def main() -> None:
    config = load_config()
    input_file = Path(config.get("input_file", "input.txt"))
    if not input_file.is_absolute():
        input_file = SCRIPT_DIR / input_file
    if not input_file.exists():
        raise FileNotFoundError(f"Input file not found: {input_file}")

    model_name = config.get("model", "gpt-4o")
    temperature = float(config.get("temperature", 0))

    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()

    llm = ChatOpenAI(model=model_name, temperature=temperature)
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
