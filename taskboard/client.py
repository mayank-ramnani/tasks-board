from .exceptions import TaskBoardError
# from .backends import get_backend // use mock for now

def get_backend(name: str):
    raise NotImplementedError("mocked in tests")

class TaskBoardClient:
    def __init__(self, backend: str, **config):
        try:
            self.backend = get_backend(backend)(**config)
        except Exception as e:
            raise TaskBoardError(f"failed to initialize backend '{backend}'") from e

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
