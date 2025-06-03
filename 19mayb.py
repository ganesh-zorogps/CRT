class Atm:
    def __init__(self,initialbal=0):
        self.bal=initialbal
    def deposit(self):
        amount=int(input("enter the money to be deposited"))
        self.bal+=amount
        print(f"{amount} deposited successfully")
        print(f"new balance{self.bal}")
    def withdrawl(self):
        amount=int(input("enter the money to be withdrwan"))
        if amount>self.bal:
            print("insufficient funds")
        else:
            self.bal-=amount
            print(f"{amount} successfully withdrawn")
            print(f"new balance{self.bal}")
    def checkbal(self):
        print(f"the available balance is {self.bal}")
    def exit():
        print("Thank u for ur service")
AtmS=Atm(initialbal=99)
while True:
    print("1.Deposit")
    print("2.Withdrawl")
    print("3.Check balance")
    print("4.exit")
    choice=int(input("enter your choice"))
    if choice==1:
        AtmS.deposit()
    elif choice==2:
        AtmS.withdrawl()
    elif choice==3:
        AtmS.checkbal
    elif choice==4:
        AtmS.exit()
    break
        

