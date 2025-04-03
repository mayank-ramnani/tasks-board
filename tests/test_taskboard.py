import taskboard
import builtins

class DummyClient(taskboard.TaskBoard):
    def get_tasks(self, list_id: str):
        return [{"id": f"{i}", "title": f"Task {i}"} for i in range(5)]

    def add_task(self, list_id: str, title: str, **kwargs):
        return "task-new"

    def delete_task(self, task_id: str):
        return True

    def update_task(self, task_id: str, **kwargs):
        return {"id": task_id, **kwargs}

    def list_task_lists(self):
        return [{"id": "inbox", "name": "Inbox"}]


def test_main_taskboard(monkeypatch):
    taskboard.get_client = lambda: DummyClient()

    client = taskboard.get_client()
    output = []

    monkeypatch.setattr(builtins, "print", lambda *args, **kwargs: output.append(" ".join(map(str, args))))

    for task in client.get_tasks("inbox"):
        print(f"[{task['id']}] {task['title']}")

    assert output == [
        "[0] Task 0",
        "[1] Task 1",
        "[2] Task 2",
        "[3] Task 3",
        "[4] Task 4",
    ]
