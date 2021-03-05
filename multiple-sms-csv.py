import os
import datetime
import csv
import africastalking as at
from dotenv import load_dotenv
# the load_dotenv function gets the environment variables defined in .env file
load_dotenv()
# assigns the variables to the environment variables
api_key = os.getenv("api_key")
username = os.getenv("username")
# Initialize the Africas Talking client with the required credentials
at.initialize(username, api_key)
# assign the sms functionality to a variable
sms = at.SMS

# create a function to parse the CSV and send a customized message
def send_messages():
    # parse the provided CSV with the inbuilt csv library
    with open('sample.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            name = row[1]
            number = row[2]
            if number != "Number":
                print(name, number)
                # Get the current date and time
                local_time = datetime.datetime.now()
                # create a customized message
                message = f"Hey {name}, this is a customized message sent on {local_time}"
                # For each entry send a customized message
                try:
                    response = sms.send(message, [number])
                    print(response)
                except Exception as e:
                    print(f'Uh oh we have a problem: {e}')
            else:
                print("Not a valid number")

send_messages()
