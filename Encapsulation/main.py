class BankAccount:

    def __init__(self):
        self._balance = 0.0

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Please entre a Valid amount")
        else:
            self._balance += amount

    def withdraw(self, amount):
        if amount >= self._balance:
            return ValueError("You don't have enough money left in your account")
        elif amount <= 0:
            raise ValueError("Withdraw amount must be postive")
        else:
            self._balance -= amount


user1 = BankAccount()
print(user1.balance)
user1.deposit(100)
print(user1.balance)
