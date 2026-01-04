# Specification: Phase I - Python CLI Todo App

## Project Overview
Build a simple, in-memory Todo application that runs in the terminal. The goal is to demonstrate Spec-Driven Development using Python and the `uv` package manager.

## Technical Stack
- **Language:** Python 3.12+
- **CLI Framework:** Typer
- **Package Manager:** uv
- **Data Storage:** In-memory (Python List/Dict)

## Functional Requirements
The CLI must support the following commands:

1. **Add Task**
   - Command: `todo add "Task description"`
   - Action: Adds a new task to the list. Default status: "Pending".

2. **List Tasks**
   - Command: `todo list`
   - Action: Displays all tasks with an ID and their current status (Pending/Done).

3. **Complete Task**
   - Command: `todo complete [ID]`
   - Action: Updates the status of the task at the given ID to "Done".

4. **Delete Task**
   - Command: `todo delete [ID]`
   - Action: Removes the task from the list.

## Non-Functional Requirements
- **No Persistence:** Data does not need to be saved to a file in this phase.
- **Error Handling:** Show a friendly message if a user tries to delete an ID that doesn't exist.
- **Code Style:** Clean, modular code generated entirely by AI.