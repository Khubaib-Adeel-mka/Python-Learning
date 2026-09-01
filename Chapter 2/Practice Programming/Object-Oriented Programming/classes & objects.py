# Create a complete Python program for a Student using OOP.

# Your program should:

# Create a class named Student.
# Use __init__() to store:
# student name
# age
# marks
# Create a method called show_info() that prints the student's details.
# Create a method called check_result():
# If marks are 50 or more, print "Pass".
# Otherwise, print "Fail".
# Create one object of the Student class.
# Call both methods using that object.

# Use this test data:

# Name: Ali
# Age: 16
# Marks: 75


class Student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks

    def show_info(self):
        print(self.name)
        print(self.age)
        print(self.marks)

    def check_result(self):
        if (self.marks>=50):
            print("Pass")
        else:
            print("Fail")


student1=Student("Khubaib",16,50)
student1.show_info()

student1.check_result()
