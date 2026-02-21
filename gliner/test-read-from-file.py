"""
GliNER: read input text from a file. Uses its own config (read-from-file-config.yaml).
"""
from pathlib import Path

import yaml
from gliner import GLiNER

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

    model_name = config.get("model", "urchade/gliner_medium-v2.1")
    threshold = float(config.get("threshold", 0.5))
    labels = config.get("labels") or ["person", "organization", "location", "date", "product", "money"]

    model = GLiNER.from_pretrained(model_name)
    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()

    entities = model.predict_entities(text, labels, threshold=threshold)

    print("=== GliNER zero-shot entities (from file) ===\n")
    for e in entities:
        print(f"  {e['text']:25} => {e['label']}")


if __name__ == "__main__":
    main()
