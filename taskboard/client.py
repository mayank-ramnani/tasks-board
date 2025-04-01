from .exceptions import TaskBoardError
from .backend_interface import TaskBoardBackend

class TaskBoardClient:
    def __init__(self, backend: TaskBoardBackend):
        """
        Initialize the TaskBoardClient with a backend.
        :param backend: Instance implementing TaskBoardBackend interface.
        """
        if not backend:
            raise TaskBoardError("backend must be provided")
        self.backend = backend

    def get_tasks(self, list_id: str):
        """Retrieve all tasks from a specific task list."""
        return self.backend.get_tasks(list_id)

    def add_task(self, list_id: str, title: str, **kwargs):
        """Add a new task to a specific list."""
        return self.backend.add_task(list_id, title, **kwargs)

    def delete_task(self, task_id: str):
        """Delete a task by ID."""
        return self.backend.delete_task(task_id)

    def update_task(self, task_id: str, **kwargs):
        """Update an existing task with new attributes."""
        return self.backend.update_task(task_id, **kwargs)

    def list_task_lists(self):
        """List all task lists available in the backend."""
        return self.backend.list_task_lists()
