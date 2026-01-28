class BankAccount:

    ROI = 10.5
    def __init__(self ,Name ,Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print("Name   : ",self.Name)
        print("Amount : ",self.Amount)

    def Deposit(self ,DepAmt):
        self.Amount += DepAmt
        print(f"{DepAmt} is added . Total available Balance is {self.Amount}")
    
    def Withdraw(self,WitAmt):
        self.Amount -=WitAmt
        print(f"{WitAmt} is added . Total available Balance is {self.Amount}")

    def CalculateInterest(self):
        Interest = (BankAccount.ROI * self.Amount)/100
        print(f"The Interest Rate is {Interest}")

obj1 = BankAccount("Harish",5000)

obj1.Display()
obj1.Deposit(2000)
obj1.Withdraw(1000)
obj1.CalculateInterest()

print("--------------------------------------------------------------------------------")
obj2 = BankAccount("Atharva",50000)

obj2.Display()
obj2.Deposit(2000)
obj2.Withdraw(1000)
obj2.CalculateInterest()


        