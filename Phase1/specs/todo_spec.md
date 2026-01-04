# Todo App Specification

## Overview
A command-line interface (CLI) application for managing tasks. The application should allow users to add, list, delete, and update tasks.

## Requirements

### Technology Stack
- Language: Python
- CLI Framework: Typer
- Dependency Management: uv

### Core Functionality

#### 1. Add Task
- Command: `add`
- Parameters:
  - `title` (required): The title of the task
  - `description` (optional): A detailed description of the task
- Behavior: Creates a new task with a unique ID and adds it to the task list

#### 2. List Tasks
- Command: `list`
- Parameters: None
- Behavior: Displays all tasks with their ID, title, description, and completion status

#### 3. Delete Task
- Command: `delete`
- Parameters:
  - `task_id` (required): The ID of the task to delete
- Behavior: Removes the specified task from the task list

#### 4. Update Task
- Command: `update`
- Parameters:
  - `task_id` (required): The ID of the task to update
  - `title` (optional): New title for the task
  - `description` (optional): New description for the task
  - `completed` (optional): New completion status for the task
- Behavior: Updates the specified fields of the task

### Data Model
- Task ID: Unique integer identifier
- Title: String (required)
- Description: String (optional)
- Completed: Boolean (default: false)
- Created At: Timestamp

### Storage
- Use in-memory storage (List/Dictionary) for simplicity
- Data persists only during the application session

### Error Handling
- Handle invalid task IDs gracefully
- Provide helpful error messages
- Validate required parameters

### Additional Features
- Display completion status with visual indicators (e.g., ✓ for completed, ○ for pending)
- Show total count of tasks when listing