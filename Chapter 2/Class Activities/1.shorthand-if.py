
# Class Activity
# Write an if-else statement and a shorthand if-else statement to check if a number is even or off and print the appropriate message.

# Simple if-else
a=int(input("Enter a Number: "))
if (a%2==0):
    print("Number is even")
else:
    print("Number is odd")

# Short-hand if-else
n=int(input("Enter a Number: "))
print("Number is even") if (n%2==0) else print("Number is odd")

