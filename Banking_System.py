import hashlib
import json
import os

# 1. LOAD DATA AT START
def load_data():
    if os.path.exists("data.json"):
        with open("data.json", "r") as f:
            return json.load(f)
    return {"users": {}, "balances": {}}

data = load_data()
users = data["users"]
balances = data["balances"]

# 2. SAVE DATA AFTER CHANGES
def save_data():
    with open("data.json", "w") as f:
        json.dump({"users": users, "balances": balances}, f)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def deposit(user):
    
    try:
        amount = int(input("Enter amount: "))
        if amount <= 0: return "Invalid amount"
        
        balances[user] += amount
        save_data() # Save to file
        return "Deposit successful"
    except ValueError:
        return "Please enter a number!"

# ... (other functions remain similar, just add save_data() where needed)
