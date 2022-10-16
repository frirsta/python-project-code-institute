import gspread
from google.oauth2.service_account import Credentials


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("python-project-code-institute")


age = SHEET.worksheet("customer_input")


def validate_data(value):
    """
    Converts user input string to integer.
    Raises ValueError if string can not be converted.
    """
    try:
        [int(value)]
    except ValueError as e:
        print(f"Invalid data: {e}, try again")
        return False
    
    return True


def get_age_data():
    """
    Get age from user.
    Executes a while loop to gather a valid string of data through the terminal.
    Must be numbers in the string.
    """
    while True:
        print("Enter age here")
        print("Data should be number")
        print("Example: 55")

        data_str = input("Enter age here: \n")

        if validate_data(data_str):
            print("Valid")
            break

    return data_str

    

age_data = [get_age_data()]


def update_woorksheet(data):
    """
    Update customer_input sheet with user input.
    """
    customer_input = SHEET.worksheet('customer_input')
    customer_input.append_row(data)
    print("Updated!")


update_woorksheet(age_data)