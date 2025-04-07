from dataclasses import dataclass
from typing import Optional

@dataclass
class Task:
    id: str
    title: str
    status: Optional[str] = None

@dataclass
class TaskList:
    id: str
    name: str
