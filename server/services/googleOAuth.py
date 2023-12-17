from google.oauth2 import service_account
from googleapiclient.discovery import build
import os

class GoogleOAuth:

    SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly'] 

    def __init__(self):
        self.clientId = os.environ.get('GOOGLE_AUTH_CLIENT_ID')
        self.clientSecret = os.environ.get('GOOGLE_AUTH_CLIENT_SECERET')
        self.refreshToken = os.environ.get('GOOGLE_AUTH_REFRESH_TOKEN')


    def create_drive_service():
        creds = service_account.Credentials.from_service_account_info(
            {'client_id': self.clientId, 'client_secret': self.clientSecret},
            scopes=SCOPES,
        )

        creds.token = ACCESS_TOKEN
        return build('drive', 'v3', credentials=creds)
