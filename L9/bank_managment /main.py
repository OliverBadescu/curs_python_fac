class BankAccount:
    def __init__(self, initial_balance=0):
        self._balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited {amount}. New balance: {self._balance}")

    def withdraw(self, amount):
        if amount > self._balance:
            print("Insufficient funds!")
        elif amount > 0:
            self._balance -= amount
            print(f"Withdrew {amount}. New balance: {self._balance}")

    def get_balance(self):
        return self._balance


account = BankAccount(100)
print(f"Initial balance: {account.get_balance()}")
account.deposit(50)
account.withdraw(30)
account.withdraw(200)
print(f"Final balance: {account.get_balance()}")
