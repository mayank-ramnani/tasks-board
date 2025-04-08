from abc import ABC, abstractmethod
from typing import List, Any
from taskboard.types import Task, TaskList

class TaskBoard(ABC):
    """
    Abstract base class for task board backends.

    This interface defines the expected behavior of any task board client.
    Concrete implementations must provide methods to retrieve, create,
    update, and delete tasks, as well as list task lists.

    Implementations may interact with services like Trello, Google Tasks, etc.
    """

    @abstractmethod
    def get_tasks(self, list_id: str) -> List[Task]:
        """
        Retrieve all tasks belonging to a specific task list.

        Args:
            list_id: The unique identifier of the task list.

        Returns:
            A list of Task objects.
        """
        ...

    @abstractmethod
    def add_task(self, list_id: str, title: str, **kwargs: Any) -> str:
        """
        Create a new task in a given task list.

        Args:
            list_id: The ID of the task list to add the task to.
            title: The title of the task.
            kwargs: Additional task metadata (e.g., status, etc).

        Returns:
            The ID of the newly created task.
        """
        ...

    @abstractmethod
    def delete_task(self, task_id: str) -> bool:
        """
        Delete a task by its ID.

        Args:
            task_id: The ID of the task to delete.

        Returns:
            True if the task was deleted, False otherwise.
        """
        ...

    @abstractmethod
    def update_task(self, task_id: str, **kwargs: Any) -> Task:
        """
        Update a task's fields by its ID.

        Args:
            task_id: The ID of the task to update.
            kwargs: Fields to update (e.g., title, status).

        Returns:
            The updated Task object.
        """

    @abstractmethod
    def list_task_lists(self) -> List[TaskList]:
        """
        Retrieve all available task lists in the backend.

        Returns:
            A list of TaskList objects.
        """
        ...

