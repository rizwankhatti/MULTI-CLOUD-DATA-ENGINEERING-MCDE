# Task 06 - Banking Ledger
class Account:
    def __init__(self, balance):
        self._balance = balance
        self.history = []                   # tuples cannot be changed

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self._balance += amount
        self.history.append((len(self.history) + 1, "deposit", amount, self._balance))

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
        self.history.append((len(self.history) + 1, "withdraw", amount, self._balance))

class Bank:
    def __init__(self):
        self.accounts = {}

    def transfer(self, a, b, amount):
        if a not in self.accounts or b not in self.accounts:
            raise ValueError("Account does not exist")
        self.accounts[a].withdraw(amount)   # fails first if there is a problem...
        self.accounts[b].deposit(amount)    # ...so we only get here when it is safe

bank = Bank()
bank.accounts["A"] = Account(1000)
bank.accounts["B"] = Account(200)
bank.transfer("A", "B", 350)
print(bank.accounts["A"].balance, bank.accounts["B"].balance)   # 650 550
print(bank.accounts["A"].history)
