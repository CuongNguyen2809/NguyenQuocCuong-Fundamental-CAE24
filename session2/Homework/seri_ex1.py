a = int(input("weight (kg) : "))
b = int(input("height (cm) : "))
b1 = 0.01 * b
print("height (m) : ", b1)
BMI = a/(b1**2)

if BMI < 16:
    print("Severely underweight")
elif BMI <= 18.5:
    print("Underweight")
elif BMI <= 25:
    print("Normal")
elif BMI <= 30 :
    print("Overweight")
else:
    print("Obese")
