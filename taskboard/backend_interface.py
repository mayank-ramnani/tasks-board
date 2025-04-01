from abc import ABC, abstractmethod

class TaskBoardBackend(ABC):
    @abstractmethod
    def get_tasks(self, list_id: str): ...

    @abstractmethod
    def add_task(self, list_id: str, title: str, **kwargs): ...

    @abstractmethod
    def delete_task(self, task_id: str): ...

    @abstractmethod
    def update_task(self, task_id: str, **kwargs): ...

    @abstractmethod
    def list_task_lists(self): ...
