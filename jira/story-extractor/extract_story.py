"""
Extract a single Jira Cloud story by issue key and save it to a text file.
Config: config.yaml in this folder. Secrets: .env (JIRA_EMAIL, JIRA_API_TOKEN).
"""
import os
import sys
from pathlib import Path

from dotenv import load_dotenv
import yaml
from jira import JIRA

# Load .env from this folder
SCRIPT_DIR = Path(__file__).resolve().parent
load_dotenv(SCRIPT_DIR / ".env")


def load_config() -> dict:
    config_path = SCRIPT_DIR / "config.yaml"
    if not config_path.exists():
        sys.exit(f"Config not found: {config_path}")
    with open(config_path, "r") as f:
        return yaml.safe_load(f)


def build_text(issue, fields: list) -> str:
    lines = []
    for field in fields:
        if field == "key":
            lines.append(f"Key: {issue.key}")
        elif field == "summary":
            lines.append(f"Summary: {issue.fields.summary or '(none)'}")
        elif field == "status":
            lines.append(f"Status: {issue.fields.status.name if issue.fields.status else '(none)'}")
        elif field == "assignee":
            a = issue.fields.assignee
            lines.append(f"Assignee: {a.displayName if a else '(unassigned)'}")
        elif field == "created":
            lines.append(f"Created: {issue.fields.created or '(none)'}")
        elif field == "updated":
            lines.append(f"Updated: {issue.fields.updated or '(none)'}")
        elif field == "description":
            lines.append("Description:")
            lines.append((issue.fields.description or "(none)").strip())
        elif field == "comments":
            lines.append("Comments:")
            comments = getattr(issue.fields.comment, "comments", None) or []
            for c in comments:
                author = getattr(getattr(c, "author", None), "displayName", None) or "?"
                created = getattr(c, "created", "") or ""
                body = (getattr(c, "body", "") or "").strip()
                lines.append(f"- {author} ({created}): {body}")
            if not comments:
                lines.append("  (none)")
        lines.append("")
    return "\n".join(lines).rstrip()


def main() -> None:
    config = load_config()
    jira_cfg = config.get("jira") or {}
    output_cfg = config.get("output") or {}
    base_url = (jira_cfg.get("base_url") or "").strip()
    issue_key = (jira_cfg.get("issue_key") or "").strip()
    output_file = (output_cfg.get("file") or "story.txt").strip()
    fields = output_cfg.get("fields") or [
        "key", "summary", "status", "assignee", "created", "updated", "description", "comments"
    ]

    if not base_url:
        sys.exit("config.yaml: jira.base_url is required")
    if not issue_key:
        sys.exit("config.yaml: jira.issue_key is required")

    email = os.environ.get("JIRA_EMAIL", "").strip()
    token = os.environ.get("JIRA_API_TOKEN", "").strip()
    if not email or not token:
        sys.exit("Set JIRA_EMAIL and JIRA_API_TOKEN in .env (see .env.example)")

    try:
        jira = JIRA(server=base_url, basic_auth=(email, token))
    except Exception as e:
        sys.exit(f"Jira connection failed: {e}")

    try:
        issue = jira.issue(issue_key)
    except Exception as e:
        sys.exit(f"Failed to fetch issue {issue_key}: {e}")

    text = build_text(issue, fields)
    out_path = Path(output_file)
    if not out_path.is_absolute():
        out_path = SCRIPT_DIR / out_path
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(text, encoding="utf-8")
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
