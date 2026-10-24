import json
from pathlib import Path

class Account:
    def __init__(self, name, email, pin, acc_number, balance=0):
        self.name = name
        self.email = email
        self.pin = pin
        self.acc_number = acc_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True, f"Rs. {amount} deposited successfully!"
        return False, "Invalid deposit amount."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True, f"Rs. {amount} withdrawn successfully!"
        return False, "Insufficient balance or invalid amount."

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "pin": self.pin,
            "acc_number": self.acc_number,
            "balance": self.balance
        }

class BankSystem:
    DATABASE = "bank_data.json"

    def __init__(self):
        self.accounts = {}
        self.load_data()

    def load_data(self):
        if Path(self.DATABASE).exists():
            with open(self.DATABASE, "r") as f:
                data = json.load(f)
                for item in data:
                    acc = Account(
                        item["name"], item["email"], item["pin"], 
                        item["acc_number"], item["balance"]
                    )
                    self.accounts[item["acc_number"]] = acc

    def save_data(self):
        data_list = [acc.to_dict() for acc in self.accounts.values()]
        with open(self.DATABASE, "w") as f:
            json.dump(data_list, f, indent=4)

    def create_account(self, name, email, pin, acc_number):
        if acc_number in self.accounts:
            return False, "Account number already exists!"
        new_account = Account(name, email, str(pin), acc_number, balance=0)
        self.accounts[acc_number] = new_account
        self.save_data()
        return True, f"Account created successfully for {name}!"

    def authenticate(self, acc_no, pin):
        acc = self.accounts.get(acc_no)
        if acc and str(acc.pin) == str(pin):
            return acc
        return None