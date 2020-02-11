import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://www.googleapis.com/auth/drive", "https://www.googleapis.com/auth/drive.file", 'https://www.googleapis.com/auth/spreadsheets', "https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets.readonly']

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)


sheet = client.open_by_url('https://docs.google.com/spreadsheets/d/1beR2CAlBQ2XBA3M1jJ1aPEfwE46eQt6LU-lzA0babxQ/edit#gid=0').sheet1
data = sheet.get_all_records()  # Get a list of all records

row = sheet.row_values(3)  # Get a specific row
col = sheet.col_values(1)  # Get a specific column
cell_list = sheet.range('A4:A25')
pprint(cell_list)
