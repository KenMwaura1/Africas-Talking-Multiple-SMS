import os
import africastalking as at
from openpyxl import load_workbook
from dotenv import load_dotenv

load_dotenv()

username = os.getenv("username")
api_key = os.getenv("api_key")

sms = at.SMS

at.initialize(username, api_key)
wb = load_workbook('sample.xlsx')
print(wb.sheetnames)
sheet1 = wb['Sheet1']
# print(sheet1['B2'].value)
names_cell_range = sheet1['B2:B4']
number_cell_range = sheet1['C2:C4']

for rows in names_cell_range:
    for r in rows:
        print(r.value)
for rows in number_cell_range:
    for r in rows:
        print(r.value)
def send_messages(self):
    recipients = ''
    name = ''
    message = f"hey from python {name}"
    try:
        response = self.sms.send(message, recipients, )
        print(response)
    except Exception as e:
        print(f"Uh oh we have a problem: {e}")
