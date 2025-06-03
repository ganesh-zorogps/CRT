'''
Paul is given an array A of length N. He must perform the following Operations on the
array sequentially:
* Choose any two integers from the array and calculate their average.
* If an element is less than the average, update it to 0. However, if the element is
greater than or equal to the average, he need not update it.
Your task is to help Paul find and return an integer value, representing the minimum
possible sum of all the elements in the array by performing the above operations. Note: An exact average should be calculated, even if it results in a decimal.

Input Format:
input1: An integer value N, representing the size of the array A.
input2: An integer array A.
Output Format:
Return an integer value, representing the minimum possible sum of all the elements
in the array by
Sample Input
5
1 2 3 4 5
Sample Output
5

N=int(input())
A=list(map(int,input().split()))
sum=0
for i in range(len(A)):
               Avg=(A[-1]+A[-2])/2
               if A[i] < Avg:
                   A[i]=0
for i in range(len(A)):
               sum+=A[i]
print(sum)
               

The function accepts two positive integers ‘r’ and ‘unit’ and
a positive integer array ‘arr’ of size ‘n’ as
its argument ‘r’ represents the number of rats present in an area,
‘unit’ is the amount of food each rat consumes and each ith element of array
‘arr’ represents the amount of food present in ‘i+1’ house number, where 0 <= i

Note:

Return -1 if the array is null
Return 0 if the total amount of food from all houses is not sufficient for all the rats.
Computed values lie within the integer range.
Example:

Input:

r: 7
unit: 2
n: 8
arr: 2 8 3 5 7 4 1 2
Output:

4
Explanation:
Total amount of food required for all rats = r * unit

= 7 * 2 = 14.

The amount of food in 1st houses = 2+8+3+5 = 18. Since, amount of food
in 1st 4 houses is sufficient for all the rats. Thus, output is 4.

r=int(input())
unit=int(input())
n=int(input())
arr=list(map(int,input().split()))
a=r*unit
for i in range(len(arr)):
    a=a-arr[i]
    if a<0:
        break
print(abs(a))

You are given a function.
int CheckPassword(char str[], int n);
The function accepts string str of size n as an argument. Implement the function which returns 1 if given string str is valid password else 0.
str is a valid password if it satisfies the below conditions.

– At least 4 characters
– At least one numeric digit
– At Least one Capital Letter
– Must not have space or slash (/)
– Starting character must not be a number
Assumption:
Input string will not be empty.

Example:

Input 1:
aA1_67
Input 2:
a987 abC012

Output 1:
1
Output 2:
0 

a=input()
ca="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lo="abcdefghijklmnopqrstuvwxyz"
sp="!@#$%^&*()_+:;""][{}?/.,<>"
nu="0987654321"
if a in ca and a in nu and a in lo and  a in sp and " " not in a and "/" not in a :
    print("1")
else:
    print("0")
s=input()
if len(s)!=10:
    print(False)
if s[-1].isalpha() and s[0:5].isalpha() and s[5:9].isdigit():
    print(True)
else:
    print(False)

Write a Python program that takes two integers n and m as input and computes
a checksum using the following logic:
•	Count how many numbers from 1 to m are not divisible by n.
•	Count how many numbers from 1 to m are divisible by n.
•	Return the difference between these two counts:
not_divisible_count - divisible_count
________________________________________
Input Format:
•	First line: An integer n (the divisor)
•	Second line: An integer m (the upper bound)
________________________________________
Output Format:
•	A single integer representing the checksum
________________________________________
Example Input
n = 3
m = 10
Example Output:
4
Explanation:
Numbers from 1 to 10:
Divisible by 3 → 3, 6, 9 → count = 3
Not divisible by 3 → 1, 2, 4, 5, 7, 8, 10 → count = 7
Checksum = 7 - 3 = 4

/
n=int(input())
m=int(input())
count1=0
for i in range(1,m+1):
    if i%n!=0:
        count1+=1

count2=0
for i in range(1,m+1):
    if i%n==0:
        count2+=1

dif=count1-count2
print(abs(dif)) 
/
for i in range(5):
    for j in range(5):
        if i==j:
            print("$",end=' ')
        else:
            print("*",end=' ')
    print()
/
for i in range(5):
    for j in range(5):
        print("*",end=' ')
    print()
/
for i in range(1,5):
    for j in range(1,5):
        print(j+(i-1)*4,end='\t')
    print( )
/
for i in range(1,5):
    for j in range(1,5):
        if i==1 or i==4 or j==1 or j==4:
            print("X",end=" ")
        else:
            print(" ",end=" ")
    print()
/    
for i in range(1,5):
    for j in range(1,5):
        if i==1 or i==4 or j==1 or j==4:
            print(j+(i-1)*4,end='\t')
        else:
            print(" ",end="\t")
    print( )        

for i in range(1,5):
    for j in range(1,5):
        if i<j:
            print(" ",end=" ")
        else:
            print("X",end=" ")
    print()
'''

for i in range(1,5):
    for j in range(1,5):
        if i<j:#i<j revere pyr
            print(" ",end=" ")
        else:
            print(j,end=" ")
    print()

