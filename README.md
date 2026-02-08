# my-test-python

- **[Entity extraction comparison](docs/entity-extraction.md)** — spaCy vs GliNER vs LLM-based (LangChain / LlamaIndex)

## Creating a virtual environment

A virtual environment keeps this project’s dependencies separate from your system Python and other projects.

### Quick Note
```
python3 -m venv .venv
source .venv/bin/activate
# Install dependencies per subproject, e.g.:
# pip install -r text-chunking/requirements.txt
# pip install -r spacy/requirements.txt
# pip install -r gliner/requirements.txt
# pip install -r llm-based-extraction/requirements.txt
```

### Option 1: Using `venv` (built into Python)

1. **Create the environment** (from the project root):

   ```bash
   python3 -m venv .venv   
   ```

   This creates a `.venv` folder in the project.

2. **Activate the environment**:

   - **macOS / Linux:**
     ```bash
     source .venv/bin/activate
     ```
   - **Windows (Command Prompt):**
     ```cmd
     .venv\Scripts\activate.bat
     ```
   - **Windows (PowerShell):**
     ```powershell
     .venv\Scripts\Activate.ps1
     ```

3. **Confirm it’s active**  
   Your prompt should start with `(.venv)`.

4. **Deactivate when finished**:
   ```bash
   deactivate
   ```

### Option 2: Using `uv` (faster alternative)

If you use [uv](https://github.com/astral-sh/uv):

```bash
uv venv
source .venv/bin/activate   # macOS / Linux
```

### Notes

- Add `.venv/` to `.gitignore` so the environment is not committed.
- Each subproject has its own `requirements.txt`; install from that folder, e.g.  
  `pip install -r text-chunking/requirements.txt`, `pip install -r spacy/requirements.txt`, `pip install -r gliner/requirements.txt`, or `pip install -r llm-based-extraction/requirements.txt`.
