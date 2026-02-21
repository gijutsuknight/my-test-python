"""
Test script for GliNER (Zero-Shot NER).
Define entity labels at runtime — no training required.
"""
from gliner import GLiNER

# Load a pretrained model (downloads on first run)
model = GLiNER.from_pretrained("urchade/gliner_medium-v2.1")

text = """
Apple Inc. was founded by Steve Jobs in Cupertino in 1976. 
The company now has a market cap of over 3 trillion dollars. Another year 1990
"""

# Define entity types at runtime (title case works well)
labels = ["person", "organization", "location", "date", "product", "money"]

entities = model.predict_entities(text, labels, threshold=0.5)

print("=== GliNER zero-shot entities ===\n")
for e in entities:
    print(f"  {e['text']:25} => {e['label']}")
