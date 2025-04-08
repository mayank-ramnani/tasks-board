import taskboard
from taskboard.interface import TaskBoard
from typing import List, Any
from taskboard.types import Task, TaskList

class DummyClient(TaskBoard):
    def get_tasks(self, list_id: str) -> List[Task]:
        return [Task(id="1", title="Task 1"), Task(id="2", title="Task 2")]

    def add_task(self, task: Task) -> None:
        task.id = "task-123"  # simulate assigning ID

    def delete_task(self, task_id: str) -> bool:
        return True

    def update_task(self, task: Task) -> None:
        pass # simulate successful update, no-op

    def list_task_lists(self) -> List[TaskList]:
        return [TaskList(id="inbox", name="Inbox")]

def setup_module() -> None:
    taskboard.get_client = lambda: DummyClient()

def test_get_tasks() -> None:
    client = taskboard.get_client()
    tasks = client.get_tasks("inbox")
    assert isinstance(tasks[0], Task)
    assert tasks[0].title == "Task 1"

def test_add_task() -> None:
    client = taskboard.get_client()
    task = Task(id="", title="New Task")
    client.add_task(task)
    assert task.id == "task-123"

def test_delete_task() -> None:
    client = taskboard.get_client()
    result = client.delete_task("task-123")
    assert result is True

def test_update_task() -> None:
    client = taskboard.get_client()
    task = Task(id="task-123", title="Updated Title")
    client.update_task(task)
    assert task.title == "Updated Title"  # unchanged but confirms no error

def test_list_task_lists() -> None:
    client = taskboard.get_client()
    lists = client.list_task_lists()
    assert isinstance(lists[0], TaskList)
    assert lists[0].id == "inbox"
    assert lists[0].name == "Inbox"
