'''
Max is having a dog . he want  to find the age of the dog 
with respect to the age of human.
he came to know that , the age of the
dog is mesured with respect to human  has a formula to proceed. 
example: 1 year of life span of dog is same as
seveen years of  life span  of human being
Now , calculate the age of MAX dog.
age of a dog
age of dog wrt to humans

ad=int(input("age of dog"))
adh=7*ad
print(f"age of dog with respect to human{adh}")



arr=list(map(int,input().split()))
N=len(arr)
count=0
for i in range(0,len(arr)):
    if(arr[i]%3==0):
        count=count+(arr[i]/3)
    elif arr[i]%3!=0:
        count=count+(arr[i]//3)+1
print(N)

print(int(count))
'''
'''
Max is planning to take part in a Diwali contest at a Diwali Party that will begin at 8
PM and will run until midnight (12 AM) i.e., for 4 hours. He also needs to travel to the
party venue within this time which takes him P minutes. The contest comprises
of N problems that are arranged in order of difficulty, with problem 1 being the
simplest and problem N being the most difficult. Max is aware that he will require 5*i
minutes to solve the ith problem.
Your task is help Max find and return an integer value, representing the number of
problems Max can solve and reach the party venue within the given time frame of 4
hours.
Note: Max will leave his home at exactly 8 PM to reach the party venue.
Input Format:
input1: An integer value N, representing the total number of problems.
input2: An integer value P, Representing the time to travel in minutes from his home
to the party venue.


pr=int(input())
tr=int(input())
tm=240
rm=tm-tr
ps=0
for i in range(0,pr+1):
        if rm>0 and rm>5*i:
            rm=rm-5*i
            ps+=1
print(ps)

a=input()
count=0
for i in a:
    if i==" ":
     count+=1
print(count)
   '''
a="hello-----world"
count=a.count("-")
n="-"*count+a.replace("-","")
print(n)
    
        
         
         
         
