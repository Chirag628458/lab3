# TODO: Define BankAccount class
class BankAccount:
# TODO: Define constructor with parameters to initialize instance attributes
    def __init__(self, new_name, checking_balance, savings_balance):
        self.name = new_name
        self.checking_balance = checking_balance
        self.savings_balance = savings_balance

# TODO: Define deposit_checking() method
    def deposit_checking(self, checkDep):
        self.checking_balance += checkDep
       # print(self.checkingBalance)

# TODO: Define deposit_savings() method
    def deposit_savings(self, selfDep):
        self.savings_balance += selfDep
        #print(self.savingsBalance)

# TODO: Define withdraw_checking()  method
    def withdraw_checking(self, checkWithdraw):
        self.checking_balance -= checkWithdraw
        #print(self.checkingBalance)
# TODO: Define withdraw_savings()  method
    def withdraw_savings(self, selfWithdraw):
        self.savings_balance -= (selfWithdraw)
# TODO: Define transfer_to_savings() method
    def transfer_to_savings(self, amount):
        self.checking_balance -= amount
        self.savings_balance += amount

account = BankAccount("Mickey", 500.00, 1000.00)
account.checking_balance = 500
account.savings_balance = 500
account.withdraw_savings(100)
account.withdraw_checking(100)
account.transfer_to_savings(300)
print(account.name)
print(f'${account.checking_balance:.2f}')
print(f'${account.savings_balance:.2f}')

