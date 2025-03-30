from .exceptions import TaskBoardError

class TaskBoardClient:
    def __init__(self, backend):
        if not backend:
            raise TaskBoardError("backend must be provided")
        self.backend = backend

    def get_tasks(self, list_id: str):
        return self.backend.get_tasks(list_id)

    def add_task(self, list_id: str, title: str, **kwargs):
        return self.backend.add_task(list_id, title, **kwargs)

    def delete_task(self, task_id: str):
        return self.backend.delete_task(task_id)

    def update_task(self, task_id: str, **kwargs):
        return self.backend.update_task(task_id, **kwargs)

    def list_task_lists(self):
        return self.backend.list_task_lists()
