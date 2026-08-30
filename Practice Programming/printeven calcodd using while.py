c=1
odd=0
while c<=100:
    if c%2==0:
        print(c)
    else:
        odd=odd+1
    c=c+1
print("Total no of odds:", odd)