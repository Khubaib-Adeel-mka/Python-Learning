
n = int(input("Enter a number to find Factorial: "))
f=1
c=1

while c<=n:
    f=f*c
    c=c+1

print("Factorial of", n,"is", f)