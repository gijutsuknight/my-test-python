"""
Test script for spaCy (Traditional NLP).
Install: pip install spacy && python -m spacy download en_core_web_sm
"""
import spacy

# Load a small English model (run: python -m spacy download en_core_web_sm)
nlp = spacy.load("en_core_web_sm")

text = "Apple Inc. was founded by Steve Jobs in Cupertino. It is now worth over 3 trillion dollars."
doc = nlp(text)

print("=== Tokens & POS ===")
for token in doc:
    print(f"  {token.text:15} {token.pos_:10} {token.dep_:12}")

print("\n=== Named entities ===")
for ent in doc.ents:
    print(f"  {ent.text:20} {ent.label_:12}")

print("\n=== Lemmas ===")
print("  ", [token.lemma_ for token in doc])
