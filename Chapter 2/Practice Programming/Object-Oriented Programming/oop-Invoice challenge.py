# Challenge 8 — Build on this

# Create a class called Product.

# Store:

# name
# price
# quantity

# Create these methods:

# show_info()
# calculate_total()
# check_expensive()

# Requirements:

# show_info() prints all three attributes.

# calculate_total() should return:

# price × quantity

# check_expensive() must call calculate_total() using self.

# If the total is 5000 or more:

# Expensive Order

# otherwise:

# Normal Order

# Use:

# Name: Keyboard
# Price: 1500
# Quantity: 4

# Also store the returned total in a variable and print it.

# Expected total:

# 6000

# This time, make sure you actually use self.calculate_total() inside check_expensive() rather than calculating price * quantity again.

class Product:
    def __init__(self, name, price, quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

    def show_info(self):
        print(self.name)
        print(self.price)
        print(self.quantity)

    def calculate_total(self):
        return self.price * self.quantity
    
    def check_expensive(self):
        if self.calculate_total() >= 5000:
            print("Expensive Order")
        else:
            print("Normal Order")

product1=Product("Keyboard", 1500, 4)

product1.show_info()
total_expense=product1.calculate_total()
print(total_expense)

product1.check_expensive()