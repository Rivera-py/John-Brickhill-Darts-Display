# John-Brickhill-Darts-Display

Software supporting a screen display for the John Brickhill Charity Darts Event

## Overview

We use the following tools:
  - **Google Sheets:** Backend data; players and scores is entered into a Google docs sheets,
  - **Google Sheets API:** The Google Sheets API is used to pull the backend data into the application, using OAUTH credentials,
  - **Python:** Application logic uses Python 3, see *requirements* section for packages used,
  - **Flask:** Flask is used for the web application.

## Development

Python unit tests, linting and style tests are run with github actions on pull request.