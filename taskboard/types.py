from dataclasses import dataclass
from typing import Optional

@dataclass
class Task:
    """
    Represents a single task within a task list.

    Fields:
        id: Unique identifier for the task.
        title: Human-readable title of the task.
        list_id: Identifier for the list that this task belongs to.
        status: Optional status string (e.g., 'todo', 'in-progress', 'done').
    """
    id: str
    title: str
    list_id: str
    status: Optional[str] = None

@dataclass
class TaskList:
    """
    Represents a list or collection of tasks.

    Fields:
        id: Unique identifier for the task list.
        name: Human-readable name of the list (e.g., 'OSPSD', 'OS', 'DSA').
    """
    id: str
    name: str
