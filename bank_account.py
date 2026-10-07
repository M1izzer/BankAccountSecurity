#Without encapsulation
class BankAccount:
    def __init__(self, account_number, owner_name, balance, pin):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance
        self.pin = pin


account = BankAccount("123456", "John", 1000, 1234)

# Anyone can directly change the data
account.balance = 999999
account.pin = 0000

print(account.balance)

#With encapsulation
class BankAccount:
    def __init__(self, account_number, owner_name, balance, pin):
        self.__account_number = account_number
        self.__owner_name = owner_name
        self.__balance = balance
        self.__pin = pin

    def check_balance(self, pin):
        if pin == self.__pin:
            print(self.__balance)
        else:
            print("Incorrect PIN")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount, pin):
        if pin == self.__pin and amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Transaction denied")


account = BankAccount("123456", "John", 1000, 1234)

account.check_balance(1234)
account.deposit(500)
account.withdraw(200, 1234)
