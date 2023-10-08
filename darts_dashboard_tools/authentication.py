# Google Sheets API authentication

import os
import json
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials


class AuthenticationHandler():
    ''' Google Sheets API authentication class '''

    def __init__(self, credential_filepath: str = "credentials.json"):
        ''' Instantiate auth handler '''
        self.scopes = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
        self.credential_filepath = os.path.realpath("credentials.json")
        return
