# Challenge 7 — Use a returned value in a decision

# Create a class called Student.

# Store:

# name
# marks1
# marks2

# Create three methods:

# show_info()
# calculate_average()
# check_result()

# Requirements:

# show_info() prints the name and both marks.
# calculate_average() should return the average of the two marks.
# check_result() should call calculate_average() itself.
# If the average is 50 or more, print "Pass".
# Otherwise print "Fail".

# Use:

# Name: Ali
# Marks 1: 70
# Marks 2: 50

# Expected average:

# 60

# The important new part is this: one method should call another method of the same object using self.

class Student:
    def __init__(self,name,marks1,marks2):
        self.name=name
        self.marks1=marks1
        self.marks2=marks2

    def show_info(self):
        print(self.name)
        print(self.marks1)
        print(self.marks2)

    def calculate_average(self):
        avg=(self.marks1+self.marks2)/2
        return avg
    
    def check_result(self):
        if self.calcu>=50:
            print("Pass")
        else:
            print("Fail")

student1=Student("Ali",70,50)

average_of_both_marks=student1.calculate_average()
print(student1.calculate_average())
student1.check_result()
