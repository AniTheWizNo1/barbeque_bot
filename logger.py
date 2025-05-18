import gspread
import json
import os
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# Define the Google Sheets access scope
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

# Load credentials from environment variable (Render-safe)
creds_dict = json.loads(os.environ["GOOGLE_CREDENTIALS"])
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
client = gspread.authorize(creds)

# Your target sheet name
SHEET_NAME = "Chatbot Logs"  # (Or whatever you named your Google Sheet)

def log_to_sheet(modality, user_query, bot_response):
    try:
        sheet = client.open(SHEET_NAME).sheet1
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Add a new row
        sheet.append_row([modality, now, user_query, bot_response])
    except Exception as e:
        print(f"[Logger Error] {e}")
