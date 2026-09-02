# Challenge 9 — Slightly harder

# Create a class called Mobile.

# Store:

# brand
# price
# discount

# Create these methods:

# show_info()
# calculate_discount()
# final_price()

# Requirements:

# show_info() prints all three attributes.

# calculate_discount() should return the discount amount:

# price × discount / 100

# final_price() must call calculate_discount() using self and return:

# price - discount amount

# Use:

# Brand: Samsung
# Price: 80000
# Discount: 10

# Then:

# Create one object.
# Call show_info().
# Store the returned final price in a variable.
# Print the final price.

# Expected final price:

# 72000

# This one tests whether you can make one returned calculation depend on another returned calculation.

class Mobile:
    def __init__ (self, brand, price, discount):
        self.brand=brand
        self.price=price
        self.discount=discount

    def show_info(self):
        print(self.brand)
        print(self.price)
        print(self.discount)

    def calculate_discount(self):
        return (self.price*self.discount)/100
    
    def final_price(self):
        return self.price - self.calculate_discount()
    



mobile1=Mobile("Samsung", 80000, 10)
mobile1.show_info()

final=mobile1.final_price()
print(final)