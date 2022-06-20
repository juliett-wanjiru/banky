class Bank_account:
    def __init__(self,account_no,account_name,name):
        self.account_no=account_no
        self.account_name=account_name
        self.name=name

    def deposit(self,amount):
        if amount<=0:
         return f" deposit {amount} should be more than zero"
        else:
          self.balance+=amount
          return f"you have deposited {amount} new balnce is {self.balance}"
          self.deposit.append(amount)



    