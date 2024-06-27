account_data = {}

def register_user():
    with open("accounts.txt", "a") as file:
        username = input("Enter username: ")
        if username in account_data:
            print(f"{username} is already taken as a username")
        else:
            password = input("Enter password: ")
            account_data[username] = password
            file.write(f"{username}:{password}\n")
            print(f"User {username} has been created")

def login_user():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in account_data and account_data[username] == password:
        print(f"You have successfully logged in as {username}")
    else:
        print("Login Failed")

def change_password():
    with open("accounts.txt", "w") as file:
        username = input("Enter username: ")
        old_password = input("Enter old password: ")
        if username in account_data and account_data[username] == old_password:
            new_password = input("Enter new password: ")
            account_data[username] = new_password
            for username, password in account_data.items():
                file.write(f"{username}:{password}\n")
            print(f"Password for {username} has been changed!")
        else:
            print("User not found or Incorrect password")

def load_account_data():
    try:
        with open("account.txt", "r") as file:
            for line in file:
                username, password = line.strip().split(":")
                account_data[username] = password
    except FileNotFoundError:
        pass

load_account_data()

while True:
    print('''Welcome
          1. Register
          2. Login
          3. Change Password
          4. Exit''')

    choice = int(input("Enter your Choose "))

    if choice == 1:
        register_user()
    elif choice == 2:
        login_user()
    elif choice == 3:
        change_password()
    elif choice == 4:
        print("Thank you!")
        break
    else:
        print("Invalid Choose")