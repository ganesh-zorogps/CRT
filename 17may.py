lst=list(map(int,input().split()))
print(lst)
#even elements
for i in range(0,len(lst)):
    if(lst[i]%2==0):
     print(lst[i],end=" ")
#odd elements
for i in range(0,len(lst)):
    if(lst[i]%2!=0):
     print(lst[i],end=" ")
         
    
        
