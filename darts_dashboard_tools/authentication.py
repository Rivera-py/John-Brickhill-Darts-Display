# Google Sheets API authentication

import os
import sys
import json
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials


class AuthenticationHandler():
    ''' Google Sheets API authentication class '''

    def __init__(
        self,
        credential_filepath: str = "credentials.json",
        token_filepath: str = "token.json",
        local_port: int = 13337
    ):
        ''' Instantiate auth handler '''
        self.scopes = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
        self.credential_filepath = os.path.realpath(credential_filepath)
        self.token_filepath = os.path.realpath(token_filepath)
        self.local_port = local_port
        self.existing_token = self.lookup_token()
        self.authenticate()

    def lookup_token(self) -> bool:
        ''' Create credentials from existing token file '''
        if os.path.exists(self.token_filepath):
            self.credentials = Credentials.from_authorized_user_file(
                self.token_filepath,
                self.scopes
            )
            print("Previous token loaded.")
            return True
        else:
            print("No existing token found, generating from credential file.")
            return False

    def refresh_token(self):
        ''' Refresh existing token '''
        # TODO: Add token refresh code.
        sys.exit("Token expired, requires refresh.")

    def is_credential_file(self):
        ''' Test credential file present '''
        if not os.path.isfile(self.credential_filepath):
            exit_msg = "Credential file {0} cannot be found."
            sys.exit(exit_msg.format(self.credential_filepath))
        else:
            print_msg = "Credential file {0} found."
            print(print_msg.format(self.credential_filepath))

    def create_token(self):
        ''' Create token from credential file '''
        self.is_credential_file()
        flow = InstalledAppFlow.from_client_secrets_file(
            self.credential_filepath,
            self.scopes
        )
        self.credentials = flow.run_local_server(port=self.local_port)
        print("Credential file loaded.")

    def authenticate(self):
        ''' Verify credentials exist and are valid '''
        if self.existing_token and not self.credentials.expired:
            self.refresh_token()
        else:
            self.create_token()

        with open(self.token_filepath, "w") as token:
            token.write(self.credentials.to_json())
