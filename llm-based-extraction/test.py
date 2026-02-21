"""
Test script for LLM-based entity extraction (LangChain).
Uses OpenAI or Gemini. Loads API keys from .env. Set LLM_PROVIDER=gemini to use Gemini.
"""
import json
import os
import re
from pathlib import Path

from dotenv import load_dotenv

# Load .env from this project folder (llm-based-extraction)
load_dotenv(Path(__file__).resolve().parent / ".env")

from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI

extraction_prompt = """
Extract all entities from the following text. For each entity, provide:
- entity_name: The name of the entity
- entity_type: The type (PERSON, ORG, PRODUCT, CONCEPT, etc.)
- description: A brief description based on context

Text: {text}

Return as JSON array.
"""

_provider = (os.environ.get("LLM_PROVIDER") or "openai").strip().lower()
if _provider == "gemini":
    if not os.environ.get("GOOGLE_API_KEY"):
        raise ValueError("Set GOOGLE_API_KEY in .env to use Gemini (https://aistudio.google.com/apikey)")
    llm = ChatGoogleGenerativeAI(model=os.environ.get("LLM_MODEL") or "gemini-2.0-flash", temperature=0)
else:
    llm = ChatOpenAI(model=os.environ.get("LLM_MODEL") or "gpt-4o", temperature=0)
prompt = PromptTemplate.from_template(extraction_prompt)
chain = prompt | llm

text = """
Apple Inc. was founded by Steve Jobs in Cupertino in 1976.
The company now has a market cap of over 3 trillion dollars.
"""

if __name__ == "__main__":
    response = chain.invoke({"text": text})
    content = response.content.strip()

    # Extract JSON if wrapped in markdown code block
    json_match = re.search(r"```(?:json)?\s*([\s\S]*?)```", content)
    if json_match:
        content = json_match.group(1).strip()
    raw = content

    try:
        entities = json.loads(content)
    except json.JSONDecodeError:
        entities = []
        print("Raw response (JSON parse failed):\n", raw[:500])

    print("=== LLM-based entity extraction ===\n")
    for e in entities:
        name = e.get("entity_name", "")
        etype = e.get("entity_type", "")
        desc = e.get("description", "")
        print(f"  {name} ({etype})")
        if desc:
            print(f"    → {desc}")
        print()
