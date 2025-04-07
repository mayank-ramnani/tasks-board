from abc import ABC, abstractmethod
from typing import List, Any
from taskboard.types import Task, TaskList

class TaskBoard(ABC):
    @abstractmethod
    def get_tasks(self, list_id: str) -> List[Task]:
        """Return list of task dicts for a given list ID."""
        ...

    @abstractmethod
    def add_task(self, list_id: str, title: str, **kwargs: Any) -> str:
        """Add a task and return its unique ID."""
        ...

    @abstractmethod
    def delete_task(self, task_id: str) -> bool:
        """Delete task and return success status."""
        ...

    @abstractmethod
    def update_task(self, task_id: str, **kwargs: Any) -> Task:
        """Update task and return updated task data."""

    @abstractmethod
    def list_task_lists(self) -> List[TaskList]:
        """Return list of available task lists."""
        ...

