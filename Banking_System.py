import hashlib

users = {}
balances = {}


# HASH PASSWORD
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# REGISTER
def register():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in users:
        return "Username already exists"

    users[username] = hash_password(password)
    balances[username] = 0

    return "Account created successfully"


# LOGIN
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username not in users:
        return None

    if users[username] != hash_password(password):
        return None

    return username


# DEPOSIT
def deposit(user):
    amount = int(input("Enter amount: "))

    if amount <= 0:
        return "Invalid amount"

    balances[user] += amount
    return "Deposit successful"


# WITHDRAW
def withdraw(user):
    amount = int(input("Enter amount: "))

    if amount <= 0:
        return "Invalid amount"

    if amount > balances[user]:
        return "Not enough balance"

    balances[user] -= amount
    return "Withdraw successful"


# CHECK BALANCE
def check_balance(user):
    print("Your balance is:", balances[user])


# DELETE ACCOUNT
def delete_account(user):
    if user not in users:
        return "User not found"

    del users[user]
    del balances[user]

    return "Account deleted successfully"


# MAIN MENU
while True:

    print("\n1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print(register())

    elif choice == "2":
        user = login()

        if user:
            while True:
                print("\n--- ACCOUNT MENU ---")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Check Balance")
                print("4. Delete Account")
                print("5. Logout")

                option = input("Choose: ")

                if option == "1":
                    print(deposit(user))

                elif option == "2":
                    print(withdraw(user))

                elif option == "3":
                    check_balance(user)

                elif option == "4":
                    print(delete_account(user))
                    break

                elif option == "5":
                    break

    elif choice == "3":
        break
