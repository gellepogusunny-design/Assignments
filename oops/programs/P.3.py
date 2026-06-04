# encapsulation.py
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance   # "private" attribute (name-mangled)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return amount
        raise ValueError("Insufficient funds")

    # getter using property
    @property
    def balance(self):
        return self.__balance

acct = BankAccount("Anita", 1000)
acct.deposit(500)
print(acct.balance)  # 1500
# acct.__balance  # AttributeError: private attribute
