def print_nat(n):
    fact=n
    if(n==1):
        return 1
    else:
         fact=fact*print_nat(n-1)
         return fact
n=print_nat(5)
print(n)
