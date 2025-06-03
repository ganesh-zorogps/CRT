'''IF and IF-ELSE Statements:
..Printing the Grade based on Marks
Program:
a=int(input("enter percentage"))
if a in range(90,100):
    print("o")
elif a in range(80,90):
    print("A+")
elif a in range(70,80):
    print("A")
elif a in range(60,70):
    print("B+")
elif a in range(50,60):
    print("B")
elif a in range(0,50):
    print("fail")

..Set the available balance as 5000.Ask the user the amount they want to withdraw. Allow the withdrawl process if it satisfy with the available balance.After that process show the updated balance to the user.
Program:
availablebalance=5000
AmtW=int(input("enter the amount to withdraw"))
a=availablebalance-AmtW
if availablebalance>AmtW:
         print("Withdrawl in process")
         print("updated balance",a)
else:
    print("insufficient balance")
    print("updated balance",availablebalance)

..Print the given number is even or odd
Program:
a=int(input("enter the number")
if a%2==0:
    print("even")
else:
    print("even")

FOR LOOP:
..Squares of numbers in range
Program:
for i in range(0,30):
    i=i**2
    print(i)

..Print first 10 natural numbers
Program:
for i in range(1,11):
    print(i)
Note: for printing in single line use end in the print i.e. print(i,end" ")

..Print first 50 even numbers
for i in range(0,50):
    if i%2==0:
        print(i,end=" ") 

..Print first 50 even numbers without using if condition
Program:
Even:
for i in range(0,50,2):
        print(i,end=" ")
Odd:
for i in range(1,50,2):
        print(i,end=" ")

..Print the values from 0 to 100 in reverse order
Program:
for i in range(100,-1,-1):
        print(i,end=" ")
Even:
for i in range(100,-1,-2):
        print(i,end=" ")
Odd:
for i in range(101,-1,-2):
        print(i,end=" ")
WHILE LOOP:

Example:
i=100
while(i>0):
    i=i-5
    print(i,end=" ")
    i=i+5
..Print 100 to 1 natural numbers in while loop
Program:
i=101
while(i>1):
    i=i-1
    print(i,end=" ")
1 to 100:
i=0
while(i<100):
    i=i+1
    print(i,end=" ")

LIST:
..Append the positive elements to another list
PROGRAM:
ip=[-2,5,6,-9,-12,16]
pos=[]
neg=[]
for i in range(0,len(ip)):
    if ip[i]>0:
     pos.append(ip[i])
    if ip[i]<0:
         neg.append(ip[i])
print(pos)
print(neg)

..Factorial using recursion
def print_fact(n):
    fact=n
    if(n==1):
        return 1
    else:
         fact=fact*print_nat(n-1)
         return fact
n=print_fact(5)
print(n)

OOPS CONCEPT
..Calci 
class Calci:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
    def mul(a,b):
        return a*b
    def div(a,b):
        return a/b
obj=Calci
n=int(input("enter a num "))
if n==1:
 print(obj.add(10,20))
elif n==2:
 print(obj.sub(30,20))
elif n==3:
 print(obj.mul(10,20))
elif n==4:
 print(obj.div(60,20))
else:
    print("enter a valid number")
'''
