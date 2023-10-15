# Google Sheet Data

import sys
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build


class DataHandler():
    ''' Google Sheets data handler '''

    def __init__(self, sheet_id: str, api_version: str = "v4", sheet_range: str = "ORIGINAL!A2:X67"):
        ''' Instantiate data handler '''
        self.sheet_id = sheet_id
        self.sheet_range = sheet_range
        self.api_version = api_version

    def set_build(self, credentials: Credentials):
        ''' Set build service '''
        self.service = build("sheets", self.api_version, credentials=credentials)

    def get_input_data(self):
        ''' Pull data via API '''
        output = self.service.spreadsheets().values().get(spreadsheetId=self.sheet_id, range=self.sheet_range).execute()
        self.data = output.get("values", [])
    
    def is_input_not_empty(self): # Change these is functions to output boolean and exit on validate function
        ''' Verify data exists '''
        if not self.data:
            sys.exit("No data found.")
    
    def is_input_correct_format(self):
        ''' Verify input data is correct schema '''
        print("TODO: Add schema functionality.")
    
    def validate_input_data(self):
        ''' Validate input data '''
        self.is_input_not_empty()
        self.is_input_correct_format()
    
    def scan_input_data(self) -> list:
        ''' Pull and validate input data '''
        self.get_input_data()
        self.validate_input_data()

        return self.data

    def transform_output_data(self):
        ''' Transform data to output format '''
        print("TODO: Add transform functionality.")

    def validate_output_data(self):
        ''' Validate output data '''
        print("TODO: Add data output functionality.")
