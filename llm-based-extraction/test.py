"""
Test script for LLM-based entity extraction (LangChain).
Uses OpenAI to extract entities with types and descriptions.
Loads OPENAI_API_KEY from the project .env file or the environment.
"""
import json
import re
from pathlib import Path

from dotenv import load_dotenv

# Load .env from project root (parent of llm-based-extraction)
load_dotenv(Path(__file__).resolve().parents[1] / ".env")

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

extraction_prompt = """
Extract all entities from the following text. For each entity, provide:
- entity_name: The name of the entity
- entity_type: The type (PERSON, ORG, PRODUCT, CONCEPT, etc.)
- description: A brief description based on context

Text: {text}

Return as JSON array.
"""

llm = ChatOpenAI(model="gpt-4o", temperature=0)
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
