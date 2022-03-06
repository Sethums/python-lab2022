class Bank:
    def __init__(self,num=0,n='user',t='normal',b=0):
        self.accnum=num
        self.name=n
        self.type=t
        self.bal=b
    def deposit(self):
        d=float(input("\nEnter deposit amount:"))
        self.bal=self.bal+d
        print("\nDeposited amount is %f"%(d))
    def withdraw(self):
        w=float(input("\nenter amount to withdraw:"))
        if self.bal>w:
            self.bal=self.bal-w
            print("\nWithdraw amount:%f"%(w))
        else:
            print("\nLow balance")
    def display(self):
        print("\nAccount number:",self.accnum)
        print("\nName:",self.name)
        print("\ntype:",self.type)
        print("\nbalance:",self.bal)
        
try:
    b1=Bank(102,'Anu','FixedDeposit',70000)
    b1.deposit()
    b1.withdraw()
    b1.display()
except Exception as e:
    print(e)
