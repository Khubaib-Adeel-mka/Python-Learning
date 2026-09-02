# Next challenge — slightly harder
# Create a class named Car.

# It should store:

# brand
# model
# speed

# Create two methods:

# show_info()
# check_speed()

# show_info() should display all three attributes.

# check_speed() should print:

# "Fast"

# if speed is 100 or more, otherwise:

# "Normal"

# Use:

# Brand: Toyota
# Model: Corolla
# Speed: 120

# Create one object and call both methods.

class Car:
    def __init__(self,brand,model,speed):
        self.brand=brand
        self.model=model
        self.speed=speed

    def show_info(self):
        print(self.brand)
        print(self.model)
        print(self.speed)

    def check_speed(self):
        if (self.speed>=100):
            print("Fast")
        else:
            print("Normal")

car1=Car("Toyota","Corolla", 120)
car1.show_info()
car1.check_speed()