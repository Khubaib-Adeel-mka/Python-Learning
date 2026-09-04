

# To just read the students.txt:
with open("students.txt","r") as file:
    content=file.read()
    print(content)

# To append "Khuabib" at the end of students.txt:
with open("students.txt", "a") as file:
    content=file.write("Khubaib\n")


with open("students.txt","r"):
    content=file.read()
    print(content) 

# with open("students.txt", "a") as file:
#     content=file.write("Ahmed")

# with open("students.txt","r") as file:
#     content=file.read()
#     print(content)




# Suppose you write:
# name = "Ali"
# marks = 90

# These values exist while the program is running.
# But after the program ends, those variables disappear from memory.

# What if you want the marks to remain stored?

# You need a file.
# For example:

# students.txt



# Think of it this way:

# Variable
#    │
#    │ temporary
#    ↓
# Computer Memory (RAM)
#    │
#    │ program closes
#    ↓
# Data disappears

# But:

# Python Program
#       │
#       ↓
#     File
# students.txt
#       │
#       ↓
# Data remains stored