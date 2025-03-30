from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os.path, pickle

SCOPES = ['https://www.googleapis.com/auth/tasks']

def get_service():
    creds = None
    if os.path.exists('token.pickle'):
        with open('../token.pickle', 'rb') as f:
            creds = pickle.load(f)
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file('../credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as f:
            pickle.dump(creds, f)
    return build('tasks', 'v1', credentials=creds)

service = get_service()
results = service.tasklists().list().execute()
for item in results.get('items', []):
    print(item['title'])
