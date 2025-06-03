'''
Encapsulation
class Onepiece:
    def __init__(self,navy):  #default constructor
        self.navy=navy
        self.__navy=navy #priavte a variable
    def getter(self):
        return self.__navy
    def setter(self,navy):
        self.__navy=navy
Oda=Onepiece(20)
Oda.setter(80)
Luffy=Oda.getter()
print(Luffy)

Abstraction
from abc import ABC,abstractmethod

class four_wheeler(ABC):
    @abstractmethod
    def engine():
        return "This engine consists of 4 valve cylinders"  #it will not print this unnecesary info
class Endeavour(four_wheeler):
    def car_start():
        return "car is moving"
car_1=Endeavour
ans=Endeavour.car_start()
print(ans)

Single inheritance
class father:
    def father_meth():
        return "this a father method"
class child(father):
    def child_meth():
        return "this is a child method"
parent_obj=father
child_obj=child
print(parent_obj.father_meth())
print(child_obj.child_meth())
print(child_obj.father_meth())

Multiple inheritance
class father:
    def father_meth():
        return "this a father method"
class mother:
    def mother_meth():
        return "this is a mother method"
class child(father,mother):
    def child_meth():
        return "this is a child method"
father_obj=father
mother_obj=mother
child_obj=child
print(father_obj.father_meth())
print(mother_obj.mother_meth())
print(child_obj.child_meth())
print(child_obj.father_meth())
print(child_obj.mother_meth())

Hybrid inheritance

class grandfather:
    def grandfather_meth():
        return "this a grandfather method"
class father(grandfather):
    def father_meth():
        return "this is a father method"
class mother():
    def mother_meth():
        return "this is a mother method"    
class child(father,mother):
    def child_meth():
        return "this is a child method"
grandfather_obj=grandfather
father_obj=father
mother_obj=mother
child_obj=child
print(grandfather_obj.grandfather_meth())
print(father_obj.father_meth())
print(father_obj.grandfather_meth())
print(mother_obj.mother_meth())
print(child_obj.child_meth())
print(child_obj.grandfather_meth())
print(child_obj.father_meth())
print(child_obj.mother_meth())


class Animal:
    def speak():
        return "Animal is speaking"
class Bird():
    def speak(Animal):
        return "Bird is speaking"
animal_obj=Animal
bird_obj=Bird
print(animal_obj.speak())
print(bird_obj.speak())
'''
'''
n=3456
sum=0
while n>0:
    digit=n%10
    sum=(digit*digit)+sum
    n=n//10
print(sum)
      
    
class Atm:
    def __init__(self,initialbal=0):
        self.__bal=initialbal
    def working():
        pass
class deposit(Atm):
    def deposit_amt(self):
        amount=int(input("enter the money to be deposited"))
        self.__bal+=amount
        print(f"{amount} deposited successfully")
        print(f"new balance{self.__bal}")
class withdrawl(Atm):
    def withdrawl_amt(self):
        amount=int(input("enter the money to be withdrawn"))
        if amount>self.__bal:
            print("insufficient funds")
        else:
            self.__bal-=amount
            print(f"{amount} successfully withdrawn")
            print(f"new balance{self.__bal}")
class checkbal(Atm):
    def availbal(self):
        print(f"the available balance is {self.__bal}")
class exit():
        print("Thank u for ur service")
AtmS=Atm(initialbal=99)
depo=deposit
withdraw=withdrawl
avaiabal=checkbal
back=exit
while True:
    print("1.Deposit")
    print("2.Withdrawl")
    print("3.Check balance")
    print("4.exit")
    choice=int(input("enter your choice"))
    if choice==1:
        depo.deposit_amt()
    elif choice==2:
        withdraw.withdrawl_amt()
    elif choice==3:
        availabal.availbal
    elif choice==4:
        back.exit()
    break    


class details:
    def __init__(self,name,bal ):
        self.name=name
        self.__bal=0
    def deposit(self,deposit_amount):
        amt=int(input("enter the amount to be deposited"))
        if amt>0:
          self.__bal+=amt
          print(f"{amt} deposited successfully")
          print(f"new balance{self.__bal}")
        else:
            print("enter a valid input")
    def withdraw(self,withdraw_amount):
        amt=int(input("enter the amount to be deposited"))
        if amt<=self.__bal:
          self.__bal-=amt
          print(f"{amt} deposited successfully")
          print(f"new balance{self.__bal}")
        else:
            print("insufficient funds")
    def get_bal(self):
        return self.__bal
Atms=details(name="ganesh",bal=5000)
while True:
    print("1.Deposit")
    print("2.Withdrawl")
    print("3.Check balance")
    print("4.exit")
    choice=int(input("enter your choice"))
    if choice==1:
        Atms.deposit_amt()
    elif choice==2:
        Atms.withdrawl_amt()
    elif choice==3:
        Atms.availbal
    elif choice==4:
        Atms.exit()
    break    

arr=[9,8,-55,-89,16,10]
arr.sort()
print(f"minimum element is {arr[0]}")

print(f"maximum element is {arr[-1]}")
sum=arr[0]+arr[-1]
print(sum)
'''
