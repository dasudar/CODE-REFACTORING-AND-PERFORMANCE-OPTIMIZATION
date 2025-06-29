import typer
from tasks import TaskManager

app = typer.Typer()
manager = TaskManager()

@app.command()
def add(task: str):
    """Add a new task."""
    manager.add_task(task)
    typer.echo("Task added.")

@app.command()
def list():
    """List all tasks."""
    tasks = manager.get_tasks()
    if not tasks:
        typer.echo("No tasks found.")
    for i, task in enumerate(tasks, 1):
        typer.echo(f"{i}. {task}")

@app.command()
def remove(index: int):
    """Remove a task by its index."""
    if manager.remove_task(index - 1):
        typer.echo("Task removed.")
    else:
        typer.echo("Invalid index.")

if __name__ == "__main__":
    app()