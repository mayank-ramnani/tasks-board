# Tasks Board
- This repository defines a unified API to interact with various task board backends like Trello, Google Tasks, etc

## Google Tasks Implementation
This module implements a `TaskBoard` interface using the Google Tasks API, enabling pluggable integration with a standard task board abstraction.

### Features
- List task lists (`TaskList`)
- List tasks in a list
- Add a new task
- Update existing tasks
- Delete tasks

### Requirements
- Python 3.10+
- Google Tasks API enabled
- `credentials.json` (from Google Cloud Console)
- `token.pickle` (OAuth2 token, generated on first run)

### Setup
1. Install dependencies:
```bash
uv pip install google-api-python-client google-auth google-auth-httplib2 google-auth-oauthlib
```
2. Place your credentials.json in the project root.
3. Run once to trigger the OAuth flow and generate token.pickle:
`uv run pytest tests/test_google_tasks.py`

### Usage
Use the get_client() function from taskboard to get an authenticated Google Tasks backend:
```py
from taskboard import get_client

client = get_client()
lists = client.get_task_lists()
tasks = client.get_tasks(lists[0].id)
```
