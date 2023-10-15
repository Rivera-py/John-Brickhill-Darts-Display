# Control plane for darts dashboard app

import argparse
from darts_dashboard_tools import authentication
from darts_dashboard_tools import data


parser = argparse.ArgumentParser()
parser.add_argument("-s", "--sheet_id", help="Google sheet ID.")
arguments = parser.parse_args()

if __name__ == '__main__':
    credentials = authentication.AuthenticationHandler().credentials
    data = data.DataHandler(arguments.sheet_id)
    data.set_build(credentials)
    print(data.scan_input_data())
