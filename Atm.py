bal=10000
Op=int(input("enter a number"))
while(Op<=4):
 if Op==1:
    Dp=int(input("enter the money"))
    bal=bal+Dp
    print("Available balance=",bal)
 elif Op==2:
    wd=int(input("enter the money"))
    if bal<=0:
         bal=0
         print("Avaialable balance=",bal)
    else:
        bal=bal-wd
        print("Avaialable balance=",bal)
 elif Op==3:
     bal=bal
     print("Available balance=",bal)
 else:
    print("please insert your card")
 if bal<=0:
     print("insufficient funds")
 
    
          
