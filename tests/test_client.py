from typing import Generator
import pytest
from unittest.mock import MagicMock
from taskboard.client import TaskBoardClient
from taskboard.backend_interface import TaskBoardBackend

@pytest.fixture # type: ignore[misc]
def mock_backend() -> Generator[MagicMock, None, None]:
    backend = MagicMock(spec=TaskBoardBackend)
    backend.get_tasks.return_value = [{"id": "t1", "title": "Task 1"}]
    backend.add_task.return_value = "new-task-id"
    backend.delete_task.return_value = True
    backend.update_task.return_value = {"id": "t1", "title": "Updated"}
    backend.list_task_lists.return_value = [{"id": "l1", "name": "Inbox"}]
    yield backend


def test_get_tasks(mock_backend: MagicMock) -> None:
    client = TaskBoardClient(backend=mock_backend)
    result = client.get_tasks("list-id")
    assert result == [{"id": "t1", "title": "Task 1"}]
    mock_backend.get_tasks.assert_called_once_with("list-id")


def test_add_task(mock_backend: MagicMock) -> None:
    client = TaskBoardClient(backend=mock_backend)
    result = client.add_task("list-id", "New Task", priority="high")
    assert result == "new-task-id"
    mock_backend.add_task.assert_called_once_with("list-id", "New Task", priority="high")


def test_delete_task(mock_backend: MagicMock) -> None:
    client = TaskBoardClient(backend=mock_backend)
    result = client.delete_task("task-id")
    assert result is True
    mock_backend.delete_task.assert_called_once_with("task-id")


def test_update_task(mock_backend: MagicMock) -> None:
    client = TaskBoardClient(backend=mock_backend)
    result = client.update_task("task-id", title="Updated")
    assert result == {"id": "t1", "title": "Updated"}
    mock_backend.update_task.assert_called_once_with("task-id", title="Updated")


def test_list_task_lists(mock_backend: MagicMock) -> None:
    client = TaskBoardClient(backend=mock_backend)
    result = client.list_task_lists()
    assert result == [{"id": "l1", "name": "Inbox"}]
    mock_backend.list_task_lists.assert_called_once_with()
