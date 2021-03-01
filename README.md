[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![GPL license](https://img.shields.io/badge/License-GPL-blue.svg)](http://perso.crans.org/besson/LICENSE.html)
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
# Africas-Talking-Multiple-SMS 
This is a simple script utilizing python and the Africas Talking to send bulk texts from a excel sheet.
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
3. Ensure the spreadsheet is in the same folder as the script
 
4. Create a `.env` file and add your credentials 
   OR Copy the included example
   
    `cp .env-example .env `
5. Add your credentials to the .env file

6. Install the required dependencies
   
    `pip Install -r requirements`
7. Run the script 

    `python multiple-sms.py`


