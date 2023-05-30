class Account():
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
    def deposit(self,dep_amt):
        self.balance=self.balance +dep_amt
        print (f" Added: {dep_amt} Deposit Accepted")
    def withdraw(self,wd_amt):
        if self.balance >=wd_amt:
            self.balance=self.balance - wd_amt
            print("withdraw accepted")
        else:
            print("Sorry not enough funds!")
    
    def __str__(self) -> str:
        return f"Account owner:{self.owner } \nbalance : { self.balance}"   
acct1= Account('jose',100)
print(acct1)
print(acct1.balance)
print(acct1.owner)
print(acct1.deposit(50))
print(acct1.balance)
print(acct1.withdraw(100))
print(acct1.balance)
