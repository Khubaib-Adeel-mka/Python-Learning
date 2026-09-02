# Challenge 6 — Deposit + Withdraw

# Let's increase the difficulty slightly without introducing a new OOP topic yet.

# Create a class called BankAccount.

# Store:

# name
# balance

# Create three methods:

# show_balance()
# deposit(amount)
# withdraw(amount)

# Requirements:

# show_balance() prints the name and current balance.
# deposit(amount) adds amount to the balance.
# withdraw(amount):
# If amount <= balance, subtract it from the balance.
# Otherwise print "Insufficient Balance".

# Use:

# Name: Ali
# Starting Balance: 5000

# Then perform these operations in this order:

# Show balance
# Deposit 2000
# Withdraw 3000
# Show balance

# The final balance should be:

# 4000

# Try it without looking back at your previous BankAccount solution.


class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance

    def show_balance(self):
        print(self.name)
        print(self.balance)

    def deposit(self, amount):
        self.balance=self.balance+amount
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance=self.balance-amount
        else:
            print("Insufficient Balance")


name1=BankAccount("Ali", 5000)
name1.show_balance()

name1.deposit(2000)
name1.withdraw(3000)

name1.show_balance()