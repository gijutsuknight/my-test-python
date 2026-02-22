"""
REBEL relationship extraction: read input text from a file.
Uses read-from-file-config.yaml. Extracts (head, type, tail) triplets.
"""
from pathlib import Path

import yaml
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

from triplets import extract_triplets

SCRIPT_DIR = Path(__file__).resolve().parent
CONFIG_FILE = SCRIPT_DIR / "read-from-file-config.yaml"


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

    model_name = config.get("model", "Babelscape/rebel-large")
    max_length = int(config.get("max_length", 256))
    num_beams = int(config.get("num_beams", 3))
    num_return_sequences = int(config.get("num_return_sequences", 3))

    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    gen_kwargs = {
        "max_length": max_length,
        "length_penalty": 0,
        "num_beams": num_beams,
        "num_return_sequences": num_return_sequences,
    }

    inputs = tokenizer(text, max_length=max_length, padding=True, truncation=True, return_tensors="pt")
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

    print("=== REBEL relationship extraction (from file) ===\n")
    for t in all_triplets:
        print(f"  ({t['head']}, {t['type']}, {t['tail']})")


if __name__ == "__main__":
    main()
