import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# Name of your Google Sheet
SHEET_NAME = "Formi-Chatbot-Logs"

def log_to_sheet(modality, user_input, response):
    # Google Sheets API scope
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]
    # Load credentials from JSON (place it in the same folder as logger.py)
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)

    sheet = client.open(SHEET_NAME).sheet1

    # Append a row with modality, timestamp, user query, and response
    sheet.append_row([
        modality,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        user_input,
        response
    ])
