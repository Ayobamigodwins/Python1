# BANK ACCOUNT HOLDER CLASS
class account_holder :
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance 
        print(f"Account created for {self.name} with initial balance: {self.balance}")

    def deposit(self, amount1):
        self.amount1 = amount1
        print(f"{self.amount1} deposited. New balance: {self.balance} + {self.amount1} = {self.balance + self.amount1}. ")

    def withdraw(self, amount):
        if amount > self.balance + self.amount1:
            print(f"Insufficient funds for withdrawal. Current balance: {self.balance + self.amount1}.")
        else:
            self.amount = amount
            print(f"{self.amount} withdrawn. New balance: {self.balance + self.amount1} - {self.amount} = {self.balance + self.amount1 - self.amount}.")    
# Example usage
account1 = account_holder("Alice", 1000)
account1.deposit(500)
account1.withdraw(2000)

account2 = account_holder("Bob", 500)
account2.deposit(300)   
account2.withdraw(600)
