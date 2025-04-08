from .interface import TaskBoard
from .types import Task, TaskList
from collections.abc import Callable

get_client: Callable[[], TaskBoard] = lambda: NotImplemented

__all__ = ["TaskBoard", "Task", "TaskList", "get_client"]
