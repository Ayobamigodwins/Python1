number = int(input("Enter a number: "))
if number <= 1:
    print("The number is not prime.")
else:
    for i in range(2, number):
        if number % i == 0:
            print("The number is not prime.")
            break
    else:
        print("The number is prime.")
    