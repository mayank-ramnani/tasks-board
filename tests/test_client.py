import pytest
from unittest.mock import patch, MagicMock
from taskboard.client import TaskBoardClient

@pytest.fixture
def mock_backend():
    backend = MagicMock()
    backend.get_tasks.return_value = ["task1", "task2"]
    backend.add_task.return_value = "new-task-id"
    backend.delete_task.return_value = True
    backend.update_task.return_value = {"status": "done"}
    backend.list_task_lists.return_value = ["list1", "list2"]
    return backend

@patch("taskboard.client.get_backend")
def test_get_tasks(mock_get_backend, mock_backend):
    mock_get_backend.return_value = lambda **cfg: mock_backend
    client = TaskBoardClient("fake")
    tasks = client.get_tasks("abc")
    assert tasks == ["task1", "task2"]
    mock_backend.get_tasks.assert_called_once_with("abc")

@patch("taskboard.client.get_backend")
def test_add_task(mock_get_backend, mock_backend):
    mock_get_backend.return_value = lambda **cfg: mock_backend
    client = TaskBoardClient("fake")
    task_id = client.add_task("abc", "do the thing")
    assert task_id == "new-task-id"
    mock_backend.add_task.assert_called_once_with("abc", "do the thing")

@patch("taskboard.client.get_backend")
def test_delete_task(mock_get_backend, mock_backend):
    mock_get_backend.return_value = lambda **cfg: mock_backend
    client = TaskBoardClient("fake")
    result = client.delete_task("task123")
    assert result is True
    mock_backend.delete_task.assert_called_once_with("task123")

@patch("taskboard.client.get_backend")
def test_update_task(mock_get_backend, mock_backend):
    mock_get_backend.return_value = lambda **cfg: mock_backend
    client = TaskBoardClient("fake")
    updated = client.update_task("task123", status="done")
    assert updated == {"status": "done"}
    mock_backend.update_task.assert_called_once_with("task123", status="done")

@patch("taskboard.client.get_backend")
def test_list_task_lists(mock_get_backend, mock_backend):
    mock_get_backend.return_value = lambda **cfg: mock_backend
    client = TaskBoardClient("fake")
    lists = client.list_task_lists()
    assert lists == ["list1", "list2"]
    mock_backend.list_task_lists.assert_called_once()
