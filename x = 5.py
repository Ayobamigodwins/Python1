

#a = int(input("enter a number"))
#b = int(input("enter second number"))
#c = a + b
#d = a * b
#print (c, d)

#print("Hello, what is your name?")

#name=input()

#print("Thank you")
#x = 2
#y = 8
#if x + y >= 3:
#    print("success")
#else: 
#    print("failure")

name = input("Name of the student: ")
grade = int(input("Grade of the student: "))
if grade >= 0 and grade <= 60:
    print(name + " has a C")
if grade >= 60 and grade <= 70:
    print(name + " has a B")
elif grade >= 70 and grade <= 100: 
    print(name + " has a A")