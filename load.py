import json
import gspread

with open('credentials.json') as json_file:
     creds = json.load(json_file)
     print(creds)

gs = gspread.authorize(creds)