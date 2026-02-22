"""
Simplest REBEL test: relationship extraction with inline text.
Extracts (subject, relation, object) triplets using Babelscape/rebel-large.
"""
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

from triplets import extract_triplets

MODEL_NAME = "Babelscape/rebel-large"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

gen_kwargs = {
    "max_length": 256,
    "length_penalty": 0,
    "num_beams": 3,
    "num_return_sequences": 3,
}

text = "Steve Jobs co-founded Apple with Steve Wozniak in 1976."

inputs = tokenizer(text, max_length=256, padding=True, truncation=True, return_tensors="pt")
generated = model.generate(
    inputs["input_ids"].to(model.device),
    attention_mask=inputs["attention_mask"].to(model.device),
    **gen_kwargs,
)
decoded = tokenizer.batch_decode(generated, skip_special_tokens=False)

all_triplets = []
for sent in decoded:
    for t in extract_triplets(sent):
        if t not in all_triplets:
            all_triplets.append(t)

print("=== REBEL relationship extraction (triplets) ===\n")
for t in all_triplets:
    print(f"  ({t['head']}, {t['type']}, {t['tail']})")
