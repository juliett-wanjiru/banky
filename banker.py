
class Account:
    def __init__(self,name,acc_number):
        self.balance=0
        self.name=name
        self.acc_number=acc_number
        self.deposits=[]
        self.withdraws=[]


    def deposit(self,amount):
        if amount<=0:
            return f"deposit amount should be more than zero"
        else:
            self.balance+=amount
            self.deposits.append(self.balance)
            return f"you have deposited {amount}.Your new balnace is {self.balance}"

    def withdraw(self,amount):

        if amount > self.balance:
            return f"your balance is {self.balance} you cannot withdraw the {amount} "
        elif amount<=0:
            return  f"amount must be greater than zero"
        else:
            self.balance-=amount
            self.withdraws.append(self.balance)
            return f"you have withdrawn {amount} your blance is {self.balance}"
    def deposit_statements(self):
        print(*self.deposits,sep="\n")
    def withdraw_statements(self):
        print(*self.withdraws,sep="\n")
    
      
    

