from .interface import TaskBoard
from collections.abc import Callable

get_client: Callable[[], TaskBoard] = lambda: NotImplemented
