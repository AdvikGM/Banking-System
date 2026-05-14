import hashlib
import json
import os

# --- THE BLUEPRINT (CLASS) ---
class SimpleBankV2:
    def __init__(self):
        """
        This runs automatically when we create the bank.
        It sets up our 'folders' (dictionaries) and loads saved data.
        """
        self.filename = "bank_data.json"
        self.users = {}
        self.balances = {}
        self.load_from_file()

    def load_from_file(self):
        """Loads data from a file so we don't lose progress."""
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                data = json.load(f)
                self.users = data["users"]
                self.balances = data["balances"]

    def save_to_file(self):
        """Saves current data to a physical file."""
        with open(self.filename, "w") as f:
            json.dump({"users": self.users, "balances": self.balances}, f)

    def hash_password(self, password):
        """Same as your v1: turns '123' into a long secret string."""
        return hashlib.sha256(password.encode()).hexdigest()

    def register(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username in self.users:
            return "❌ Username already exists"

        self.users[username] = self.hash_password(password)
        self.balances[username] = 0
        self.save_to_file()  # Save changes!
        return "✅ Account created successfully"

    def login(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username not in self.users:
            return None

        if self.users[username] != self.hash_password(password):
            return None

        return username

    def deposit(self, user):
        try:
            amount = int(input("Enter amount to deposit: "))
            if amount <= 0:
                return "❌ Invalid amount"
            
            self.balances[user] += amount
            self.save_to_file()  # Save changes!
            return f"✅ Deposit successful. New balance: {self.balances[user]}"
        except ValueError:
            return "❌ Error: Please enter a whole number."

    def withdraw(self, user):
        try:
            amount = int(input("Enter amount to withdraw: "))
            if amount <= 0:
                return "❌ Invalid amount"
            if amount > self.balances[user]:
                return "❌ Not enough balance"

            self.balances[user] -= amount
            self.save_to_file()  # Save changes!
            return f"✅ Withdraw successful. New balance: {self.balances[user]}"
        except ValueError:
            return "❌ Error: Please enter a whole number."

    def delete_account(self, user):
        confirm = input(f"Type 'DELETE' to confirm removing {user}: ")
        if confirm == "DELETE":
            del self.users[user]
            del self.balances[user]
            self.save_to_file()
            return "🗑️ Account deleted successfully"
        return "Delete cancelled."

# --- THE MAIN PROGRAM (USING THE CLASS) ---

def main():
    # We create ONE instance of our bank 'blueprint'
    my_bank = SimpleBankV2()

    while True:
        print("\n=== V2 BANKING SYSTEM ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            print(my_bank.register())

        elif choice == "2":
            user = my_bank.login()

            if user:
                print(f"\nWelcome, {user}!")
                while True:
                    print("\n--- ACCOUNT MENU ---")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Check Balance")
                    print("4. Delete Account")
                    print("5. Logout")

                    option = input("Choose: ")

                    if option == "1":
                        print(my_bank.deposit(user))
                    elif option == "2":
                        print(my_bank.withdraw(user))
                    elif option == "3":
                        print(f"💰 Your balance is: {my_bank.balances[user]}")
                    elif option == "4":
                        result = my_bank.delete_account(user)
                        print(result)
                        if "deleted" in result:
                            break
                    elif option == "5":
                        break
            else:
                print("❌ Invalid login credentials.")

        elif choice == "3":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
