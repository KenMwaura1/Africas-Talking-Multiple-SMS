import csv
import africastalking as at
from dotenv import load_dotenv

with open('sample.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        name = row[1]
        number = row[2]
        print(name,number)
