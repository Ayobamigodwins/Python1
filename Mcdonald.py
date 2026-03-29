#ATM Withdrawal Simulator
balance = 1000  # starting balance

withdraw = int(input("How much would you like to withdraw? "))

if withdraw <= balance and withdraw > 0:
    balance -= withdraw
    print("Transaction approved.")
    print("Remaining balance:", balance)
else:
    print("Transaction declined.")
    print("Insufficient funds or invalid amount.")
