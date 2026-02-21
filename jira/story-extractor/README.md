# Jira story extractor

Fetches a single Jira Cloud story by issue key and saves it to a text file. All tweakable options are in `config.yaml`; secrets go in `.env`.

## Setup

1. Install dependencies (with venv active):
   ```bash
   pip install -r jira/story-extractor/requirements.txt
   ```

2. Copy `.env.example` to `.env` in this folder and set your Jira Cloud credentials:
   - **JIRA_EMAIL** — your Atlassian account email
   - **JIRA_API_TOKEN** — create at [Atlassian API tokens](https://id.atlassian.com/manage-profile/security/api-tokens)

3. Edit `config.yaml` in this folder:
   - **jira.base_url** — e.g. `https://your-domain.atlassian.net`
   - **jira.issue_key** — e.g. `PROJ-123`
   - **output.file** — path for the text file (relative to this folder or absolute). Use **{key}** and/or **{summary}** so the filename follows the story, e.g. `"{summary}.txt"` or `"{key} - {summary}.txt"`. The summary is sanitized for use as a filename.
   - **output.fields** — list of sections to include: `key`, `summary`, `status`, `assignee`, `created`, `updated`, `description`, `comments`

## Run

From the project root:

```bash
python jira/story-extractor/extract_story.py
```

Or from this folder:

```bash
python extract_story.py
```

The script writes the story to the path in `output.file` (creating parent directories if needed).
