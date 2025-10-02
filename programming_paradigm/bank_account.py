class BankAccount:
    def __init__(self, account_balance = 0):
        self.account_balance = account_balance

    def deposit(self, amount):
        self.account_balance += amount
        return self.account_balance


    def withdraw(self, amount):
        if self.account_balance>=float(amount):
            self.account_balance -= float(amount)
            return self.account_balance
        else:
            return "Insuficient funds."


    def display_balance(self):
        print(f"Current Balance: ${float(self.account_balance, 2)}")