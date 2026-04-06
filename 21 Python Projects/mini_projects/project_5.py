import json

def load_file():
    with open("passwords.json", "r") as file:
        data = json.load(file)
    return data

def update_file(password_dict):
    with open("passwords.json", "w") as passw:
        json.dump(password_dict, passw)

ATTEMPTS = 3

def create_master_password():
    master_pass = input("Please create a master Password: ")
    password_dict = {"master_password": master_pass}
    update_file(password_dict)
    print("Master Password is now Set, move to Login!")

def view_passwords():
    data = load_file()
    for acc, passw in data.items():
        if acc != "master_password":
            print(f"Account: {acc} | Password: {passw}")

def add_new_passwords():
    data = load_file()
    acc_name = input("Enter account name: ")
    acc_pass = input("Enter password: ")
    data[acc_name] = acc_pass
    update_file(data)
    print("New password has been added!")

def user_choice():
    print("Choose 1, 2 or 3: ")
    user_selection = input("1 - Add a new password, 2 - View Existing passwords, 3 - Quit: ")
    if user_selection == "1":
        add_new_passwords()
    elif user_selection == "2":
        view_passwords()
    else:
        print("You have been logged out successfully!")
        return False
    return True

def login_session():
    data = load_file()
    attempts_left = ATTEMPTS
    logged_in = False
    for i in range(ATTEMPTS):
        attempts_left -= 1
        master_pass = input("Please enter the master Password: ")
        if data["master_password"] == master_pass:
            print("Login Successful!")
            logged_in = True
            break
        elif attempts_left == 0:
            print("You are locked out for 24 Hours!")
            return
        else:
            print(f"Try Again, you have {attempts_left} attempts left!")

    if logged_in:
        while True:
            if not user_choice():
                break

try:
    with open("passwords.json", "r") as f:
        login_session()
except FileNotFoundError:
    create_master_password()
    login_session()