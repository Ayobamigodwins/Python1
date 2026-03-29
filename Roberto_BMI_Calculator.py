a = int(input("What is your weight? "))  # a = weight
b = float(input("What is your height? ")) # b = height

#Formula to calculate
BMI = a / (b * b)
print("Your BMI is", BMI)

#BMI category
if BMI < 18.5:
    print("You are underweight")
elif 18.5 <= BMI < 25:
    print("You are normal weight")
elif 25 <= BMI < 30:
    print("You are overweight")
elif BMI >= 30:
    print("You are obese")
