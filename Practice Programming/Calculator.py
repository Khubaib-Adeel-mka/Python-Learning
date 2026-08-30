
print("Welcome to My Calculator!")
print("We offer following Operations: ")

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")

op=int(input("Choose which operation you want to perform: "))

if op==1:
    print("You Chose Addition")
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    print(a,"+",b,"=", a+b)

elif op==2:
    print("You Chose Subtraction")
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    print(a,"-", b,"=", a-b)

elif op==3:
    print("You Chose Multiplication")
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    print(a,"*",b,"=", a*b)

elif op==4:
    print("You Chose Division")
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    print(a,"/",b,"=", a/b)

elif op==5:
    print("You Chose Modulus")
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    print(a,"%",b,"=", a%b)



else:
    print("Invalid input")
    print("You had to choose between 1 and 4.")

