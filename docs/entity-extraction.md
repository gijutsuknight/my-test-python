# Entity Extraction: Method Comparison

Comparison of different approaches to **entity extraction** (named entity recognition) and when to use each.

---

## 1. spaCy (Traditional NLP)

Rule-based and statistical models trained on labeled data. Runs a fixed pipeline: tokenization → POS → dependency parsing → NER.

| | |
|---|---|
| **Pros** | Fast, low cost, works offline, deterministic results |
| **Cons** | Limited to predefined entity types (e.g. PER, ORG, LOC, DATE), struggles with domain-specific entities |

**Best for:** High-volume, offline processing where standard entity types (people, orgs, places, dates) are enough and you need speed and reproducibility.

**In this repo:** See [`spacy/`](../spacy/) for a working example.

---

## 2. GliNER (Zero-Shot NER)

Transformer-based model that takes **entity type labels** at runtime (e.g. "product name", "regulation"). No per-type training; same model handles many label sets.

| | |
|---|---|
| **Pros** | Flexible entity types, no training required, handles specialized domains |
| **Cons** | Slower than spaCy, benefits from GPU for optimal performance |

**Best for:** Custom or domain-specific entity types (e.g. legal, medical, product names) without training your own NER model.

**In this repo:** See [`gliner/`](../gliner/) for a working example.

---

## 3. LLM-Based Extraction (LangChain / LlamaIndex)

Uses a large language model (via API or local) with prompts to extract entities. Can return structured output and short descriptions.

| | |
|---|---|
| **Pros** | Handles any entity type, strong context understanding, can extract descriptions and relations |
| **Cons** | Higher cost, slower, requires API access (or significant local compute) |

**Best for:** Ad-hoc or highly variable entity types, when you need rich context or descriptions, or when you already use an LLM in your pipeline.

**In this repo:** See [`llm-based-extraction/`](../llm-based-extraction/) for a working example (LangChain + OpenAI).

---

## Quick comparison

| Criteria | spaCy | GliNER | LLM-based |
|----------|--------|--------|-----------|
| **Speed** | Fastest | Medium | Slowest |
| **Cost** | Low (free, local) | Low–medium (local, optional GPU) | Higher (API or heavy local) |
| **Offline** | Yes | Yes | Depends (API vs local model) |
| **Entity flexibility** | Fixed types | User-defined types | Arbitrary types + descriptions |
| **Domain adaptation** | Needs retraining | Good out of the box | Good via prompting |
| **Determinism** | High | High | Lower (model sampling) |

---

## Choosing an approach

- **Standard NER, high throughput, offline** → spaCy  
- **Custom types, no training, domain text** → GliNER  
- **Ad-hoc types, descriptions, or already using an LLM** → LLM-based (LangChain / LlamaIndex)

---

## Hybrid approach (recommended)

The most effective pipelines combine multiple approaches:

- **Use spaCy** for standard entities (PERSON, ORG, GPE, DATE) — fast and cheap.
- **Use GliNER or LLMs** for domain-specific entities (e.g. product names, regulations, clinical terms).
- **Use LLMs** for entity description generation when you need rich context or summaries.
