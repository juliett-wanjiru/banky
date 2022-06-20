from datetime import datetime
class Account:
    def __init__(self,name,acc_number):
        self.balance=0
        self.name=name
        self.acc_number=acc_number
        self.deposits=[]
        self.withdraws=[]
        self.total=[]
        self.transaction=100



    def deposit(self,amount):
        if amount<=0:
            return f"deposit {amount} should be more than zero"
        else:
            c={'date':self.date,'amount':amount ,'naration':"deposit"}
            self.total
            print(c)
            print(self.total)

            
            
           
            self.balance+=amount
            self.deposits.append(amount)
            return f"you have deposited {amount}.Your new balnace is {self.balance}"
            
    def deposits_statement(self):
        for x in self.deposits:
            print(f"you deposited {x}")


    def withdraw(self,amount):

        if amount > self.balance:
            return f"your balance is {self.balance} you cannot withdraw the {amount} "
        elif amount<=0:
            return  f"{amount}must be greater than zero"
        else:
            c={'date':self.date,'amount':amount,'naration':"deposit"}
            self.total
            print(c)
            print(self.total)
               

            self.balance-=amount
            self.withdraws.append(amount)
            self.balance-=amount
            self.balance=self.transaction
            self.withdraws.append(amount)
        
       
            return f"you have withdrawn {amount} your blance is {self.balance}"

    def withdrawals_statement(self):
        for j in self.withdraws:
            print (f"you withdrawn {j}")

    def current_balance(self):
        balance=self.balance
        return f"your current balance is {balance}"
        
    def deposit_statements(self):
        print(*self.deposits,sep="\n")

    def withdraw_statements(self):
        print(*self.withdraws,sep="\n")

    
    def full_statement(self):
        for item in self.total:
            date=item['date']
            amount=item['amount']
            narration=item['naration']
            print(f"{date}_________ {narration}______{amount}")
# quiz 5
    def borrow (self,amount):
        if len(self.deposits)<10:
            return f"Add more deposits" 
        if amount<100:
            return f" Inquire for more than 100 loan"  
        for x in self.deposit:
            sum=0
            sum+=x["amount"]  
        if amount>sum/3:
            return f"Dear {self.name} you can borrow money up to {sum/3}" 
        if self.balance!=0:
            return f"Dear {self.name} you still have balance of {self.balance}" 
        if self.loan_balance!=0:
            return f"Dear {self.name} you still have the balance of {self.loan_balance}"
        if self.balance!=0:
            return f"Dear {self.name} you still  have balance of {self.balance}" 
        if self.loan_balance !=0:
            return f"Dear {self.name} you still have the balance of {self.loan_balance}, hence repay to borrow" 
        else:
            interest= amount*0.03
            self.loan_balance+=amount+interest
            return f"Dear {self.name} you have borrowed {self.loan_balance} and your balance is {self.balance}"
# quiz 6
    def loan_repayment(self,amount):
        if amount<0:
            return f"Amount is invald"
        if amount > self. loan_balance:
            self.balance += amount-self.loan_balance
            return f"Dear {self.name} thank you for repaying your load of {amount-self.loan_balance} and your account  balance is {self.balance}"
        else:
            self.loan_balance-=amount
            return f"Dear {self.balance} thank you, you've loan of {amount} and your current loan balance is {self.loan_balance}"

# quiz 7

    def transfer(self,amount,instance_account):
        if amount<=0:
            return f"invalid"
        if amount>= self.balance:
            return f"insufficient amount in your account"
        if isinstance(instance_account,Account):
            self.balance-=amount
            instance_account.balance += amount
            return 

        

