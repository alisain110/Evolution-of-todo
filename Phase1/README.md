# AI-Powered Todo System (Phase 1)

This is a spec-driven Python CLI application built using Claude Code and Spec-Kit Plus.

## Setup Instructions

1. **Install UV:** `curl -LsSf https://astral.sh/uv/install.sh | sh`
2. **Sync Dependencies:** `uv sync`

## How to Run

Use the following commands to manage your todos:

- **Add a Task:** `uv run src/main.py add "Title" --desc "Description"`
- **List All Tasks:** `uv run src/main.py list`
- **Complete Task:** `uv run src/main.py complete 1`
- **Delete Task:** `uv run src/main.py delete 1`

## Project Info

- **Methodology:** Spec-Driven Development (SDD)