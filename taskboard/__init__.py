from .interface import TaskBoard
from .types import Task, TaskList

from .google_tasks import GoogleTasksClient
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
import os.path
import pickle

from typing import cast, Optional

SCOPES = ["https://www.googleapis.com/auth/tasks"]

def load_credentials() -> Credentials:
    creds: Optional[Credentials] = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as f:
            creds = cast(Credentials, pickle.load(f))
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as f:
            pickle.dump(creds, f)
    return cast(Credentials, creds)

def get_client() -> TaskBoard:
    return GoogleTasksClient(load_credentials())

__all__ = ["TaskBoard", "Task", "TaskList", "get_client"]
