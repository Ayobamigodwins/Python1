class BankAccount:
    def __init__(self, account_holder, balance=0.0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited £{amount:.2f}. New balance: £{self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew £{amount:.2f}. New balance: £{self.balance:.2f}")
        else:
            print("Insufficient funds or invalid amount.")

    def check_balance(self):
        print(f"{self.account_holder}'s balance: £{self.balance:.2f}")

