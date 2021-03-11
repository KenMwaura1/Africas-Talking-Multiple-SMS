[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![GPL license](https://img.shields.io/badge/License-GPL-blue.svg)](http://perso.crans.org/besson/LICENSE.html)
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
# Africas-Talking-Multiple-SMS 
This is a simple script utilizing python and the Africas Talking API to send bulk texts from a csv and an Excel sheet.spread

Read the corresponding articles: 
- [Sending Bulk SMS using Africas Talking, Python and CSV](https://dev.to/ken_mwaura1/sending-bulk-sms-using-africas-talking-python-and-csv-5bf5)
- [Sending Bulk SMS using Africas Talking, Python and Excel](https://dev.to/ken_mwaura1/sending-bulk-sms-using-africas-talking-python-and-excel-5655)
# Points to note
This project is under current development.

Inorder to make use of it. Edit the `names_cell_range` and `number_cell_range` according to the layout of your spreadsheet

Change the name of the workbook referenced in `load_workbook()` function to your own
 
This project also uses .env file to store the API key and username. 
Both can be obtained by [signing up/logging into Africas Talking](https://www.account.africastalking.com/)
## Executing the script
1. Clone the Repo 
   
    `git clone https://github.com/KenMwaura1/Africas-Talking-Multiple-SMS`
2. Create a virtual environment (venv)
   
   `python venv venv`

 .   Activate the virtual environment
      
      `source ./scripts/activate`

If you are using [pyenv](https://github.com/pyenv/pyenv)

2a. `pyenv virtualenv at-project`

2b. `pyenv activate at-project`
3. Ensure the spreadsheet is in the same folder as the script
   
    `cd at-project`
4. Create a `.env` file and add your credentials 
   OR Copy the included example
   
    `cp .env-example .env `
5. Add your credentials to the .env file

6. Install the required dependencies
   
    `pip Install -r requirements`
7. Run the script 

    `python multiple-sms-excel.py`

    OR 
   
    `python multiple-sms-csv.py`


