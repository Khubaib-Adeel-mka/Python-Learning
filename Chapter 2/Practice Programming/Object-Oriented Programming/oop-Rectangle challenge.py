# Challenge 5 — Your first method that returns a value

# Create a class Rectangle.

# Store:

# length
# width

# Create:

# show_info()
# calculate_area()

# show_info() should print the length and width.

# calculate_area() should return:

# length × width

# Use:

# Length: 10
# Width: 5

# Then create one object, call show_info(), call calculate_area(), store the returned result in a variable called area, and print it.

# Expected:

# 10
# 5
# 50

# The new concept here is return versus print. Don't use print() inside calculate_area().

class Rectangle:
    def __init__(self, length, width):
        self.length=length
        self.width=width

    def show_info(self):
        print(self.length)
        print(self.width)

    def calculate_area(self, length,width):
        print(length*width)


length= 10
width = 5

rectangle1=Rectangle(10, 5)
rectangle1.show_info()

rectangle1.calculate_area(length,width)
