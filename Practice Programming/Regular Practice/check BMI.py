weight=float(input("Enter you Weight in Kilograms (kg): "))
height=float(input("Enter your Height in Meters (m): "))

bmi=weight/height
print("BMI = ", bmi)


if bmi<=18:
    print("You are unhealthy.")
elif bmi>18.5 and bmi<24.9:
    print("You are healthy.")
elif bmi>25:
    print("You are Overweight.")

print("")
print("")
print("If BMI <= 18, you are unhealthy.")
print("If BMI = 18.5–24.9, you are healthy.")
print("If BMI <= 25,Overweight. ")