# Control plane for darts dashboard app

from darts_dashboard_tools import authentication
from darts_dashboard_tools import data


if __name__ == '__main__':
    credentials = authentication.AuthenticationHandler().credentials
    data = data.DataHandler("")
    data.set_build(credentials)
    print(data.scan_input_data())
