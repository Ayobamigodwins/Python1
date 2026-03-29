# Bus Fare Calculator
#Task: Calculate fare based on age group.
#Example:
#Child = £1, Adult = £2.5, Senior = £1.5

age = int(input("Enter your age: "))

if age < 18:
    fare = 1
elif age < 65:
    fare = 2.5
else:
    fare = 1.5

print("Your fare is £",fare)