class BankAccount:
    def __init__(self, account_type, amount):
        self.account_type = account_type
        self.amount = amount

    def deposit(self, deposit_amount):
        self.amount += deposit_amount

    def withdraw(self, withdraw_amount):
        self.amount -= withdraw_amount

    def __str__(self):
        return "{} Amount: {}".format(self.account_type, self.amount)


sudi= BankAccount("Checkings", 100)
print(sudi.account_type)
print(sudi.amount)

sudi.deposit(30)
print(sudi.amount)

sudi.withdraw(45)
print(sudi)
print(sudi.amount)
