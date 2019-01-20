class bankaccount(object):
    def __init__(self,initial_balance=0):
        self.balance=initial_balance
    def deposit(self,amount):
        if(self.balance<=0 or amount<0):
            print("Negative Balance")
        else:
            self.balance+=amount
    def withdraw(self,amount):
        if((self.balance-amount)<0):
            print("Minimum Balance")
        else:
            self.balance-=amount;

my_account = bankaccount(15)
print ("Balance= ",my_account.balance)
my_account.withdraw(5)
print ("After Withdraw, Balance= ",my_account.balance)
my_account.deposit(54)
print ("After Deposit, Balance= ",my_account.balance)
