import os
import africastalking as at
from openpyxl import load_workbook
from dotenv import load_dotenv()

username = os.getenv("username")
api_key = os.getenv("api_key")

sms = at.SMS

at.initialize(username, api_key)
wb = load_workbook(filename='sample.xlsx')
print(wb.sheetnames)

def send_messages(self):

    recipients = ''
    name = ''
    message = f"hey from python {name}"
    try:
        response = self.sms.send(message,recipients,)
        print(response)
    except Exception as e:
        print(f"Uh oh we have a problem: {e}")
