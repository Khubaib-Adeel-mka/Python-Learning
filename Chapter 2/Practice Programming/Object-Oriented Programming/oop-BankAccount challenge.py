# Challenge 4 — Update Object Data

# Create a class called BankAccount.

# Store:

# account_holder
# balance

# Create these methods:

# show_balance()
# deposit(amount)

# show_balance() should print the account holder's name and current balance.

# deposit(amount) should add the amount to the existing balance.

# Use:

# Account Holder: Ali
# Starting Balance: 1000

# Then:

# Show the balance.
# Deposit 500.
# Show the balance again.

# Expected final balance:

# 1500

# This challenge checks whether you understand that an object's attribute can be modified through a method.

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def show_balance(self):
        print(self.account_holder)
        print(self.balance)

    def deposit(self, amount):
        self.balance=self.balance+amount

account_holder1=BankAccount("Ali", 1000)
account_holder1.show_balance()

amount=500
account_holder1.deposit(amount)
