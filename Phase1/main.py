import typer
import json
from typing import Optional
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.text import Text
from rich.prompt import Confirm

# Initialize rich console
console = Console(force_terminal=True, force_interactive=False)

# Global in-memory storage for tasks
tasks = {}
next_task_id = 1

# Task data structure
class Task:
    def __init__(self, id: int, description: str, completed: bool = False):
        self.id = id
        self.description = description
        self.completed = completed
        self.created_at = datetime.now().isoformat()

    def to_dict(self):
        return {
            'id': self.id,
            'description': self.description,
            'completed': self.completed,
            'created_at': self.created_at
        }

    def __str__(self):
        status = "X Done" if self.completed else "O Pending"
        return f"{self.id}: [{status}] {self.description}"

# Add a new task
def add_task(description: str) -> Task:
    global next_task_id
    task = Task(next_task_id, description)
    tasks[next_task_id] = task
    next_task_id += 1
    return task

# List all tasks
def list_tasks() -> list:
    return list(tasks.values())

# Complete a task by ID
def complete_task(task_id: int) -> bool:
    if task_id in tasks:
        tasks[task_id].completed = True
        return True
    return False

# Delete a task by ID
def delete_task(task_id: int) -> bool:
    if task_id in tasks:
        del tasks[task_id]
        return True
    return False

# Get a task by ID
def get_task(task_id: int) -> Optional[Task]:
    return tasks.get(task_id)

# Create a rich table for displaying tasks
def create_tasks_table(tasks_list: list) -> Table:
    table = Table(title="Todo Tasks", show_header=True, header_style="bold magenta")
    table.add_column("ID", style="dim", width=5)
    table.add_column("Status", width=10)
    table.add_column("Description", width=50)
    table.add_column("Created", width=20)

    for task in tasks_list:
        status = "X Done" if task.completed else "O Pending"
        status_style = "green" if task.completed else "yellow"
        created_time = task.created_at.split("T")[1].split(".")[0]  # Just the time part

        table.add_row(
            str(task.id),
            f"[{status_style}]{status}[/]",
            task.description,
            created_time
        )

    return table

app = typer.Typer()

@app.command()
def add(description: str):
    """Add a new task"""
    task = add_task(description)
    console.print(f"[green]Added task:[/] {task.description}", style="bold")
    console.print(f"Task ID: [blue]{task.id}[/] | Status: [yellow]Pending[/]")

@app.command()
def list_all():
    """List all tasks"""
    all_tasks = list_tasks()
    if not all_tasks:
        console.print("[yellow]No tasks found.[/]")
        return

    table = create_tasks_table(all_tasks)
    console.print(table)
    console.print(f"\n[bold]Total tasks:[/] {len(all_tasks)}")

@app.command()
def complete(task_id: int):
    """Complete a task by ID"""
    if complete_task(task_id):
        task = get_task(task_id)
        console.print(f"[green]Task {task_id} marked as complete:[/] {task.description}")
    else:
        console.print(f"[red]Task with ID {task_id} not found.[/]")

@app.command()
def delete(task_id: int):
    """Delete a task by ID"""
    if delete_task(task_id):
        console.print(f"[green]Task {task_id} deleted successfully.[/]")
    else:
        console.print(f"[red]Task with ID {task_id} not found.[/]")

def main():
    """Main entry point"""
    app()

if __name__ == "__main__":
    main()