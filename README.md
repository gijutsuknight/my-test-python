# my-test-python

## Creating a virtual environment

A virtual environment keeps this project’s dependencies separate from your system Python and other projects.

### Quick Note
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
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
- Install project dependencies after activating:  
  `pip install -r requirements.txt` (when a `requirements.txt` exists).
