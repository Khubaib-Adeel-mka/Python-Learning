a=int(input("Enter the Divident Number: "))
try:
    result=10/a
    print(result)
except ZeroDivisionError:
    print("You can't Divide any Number by Zero!")