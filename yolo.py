import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('AutoCar-33461e9e559c.json',scope)
client = gspread.authorize(creds)

sh = client.open('Autocar')
sheet = sh.get_worksheet(0)

while True:
    direction = sheet.cell(1,1).value
    print(direction)
