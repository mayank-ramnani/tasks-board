from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from typing import List
from taskboard.types import Task, TaskList
from taskboard.interface import TaskBoard

class GoogleTasksClient(TaskBoard):
    def __init__(self, credentials: Credentials):
        self.service = build("tasks", "v1", credentials=credentials)

    def get_tasks(self, list_id: str) -> List[Task]:
        result = self.service.tasks().list(tasklist=list_id).execute()
        return [
            Task(
                id=item["id"],
                title=item.get("title", ""),
                list_id=list_id,
                status=item.get("status", None),
            )
            for item in result.get("items", [])
        ]

    def add_task(self, task: Task) -> None:
        result = self.service.tasks().insert(
            tasklist=task.list_id,
            body={"title": task.title, "status": task.status or "needsAction"},
        ).execute()
        task.id = result["id"]

    def delete_task(self, task_id: str) -> bool:
        try:
            self.service.tasks().delete(tasklist="@default", task=task_id).execute()
            return True
        except Exception:
            return False

    def update_task(self, task: Task) -> None:
        self.service.tasks().update(
            tasklist=task.list_id,
            task=task.id,
            body={"id": task.id, "title": task.title, "status": task.status},
        ).execute()

    def get_task_lists(self) -> List[TaskList]:
        result = self.service.tasklists().list().execute()
        return [
            TaskList(id=item["id"], name=item["title"])
            for item in result.get("items", [])
        ]
