'''my_dict={'a':1,'b':2,'c':3}
value=my_dict.get('a')
print("value for a key",value)
keys=my_dict.keys()
print("keys in dict:",keys)

///left rotate
arr=[1,2,3,4,5]
d=2
n=len(arr)
temp=[0]*n
def rr():
    for i in range(len(arr)):
        temp[(n-d+i)%n]=arr[i]
    for i in range(len(arr)):
        temp[i]=arr[i]
    print(arr)


///right rotate
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        temp=[0]*n
        k=k%n
        for i in range(len(nums)):
            temp[(i+k)%n]=nums[i]
        for i in range(len(nums)):
            nums[i]=temp[i]
    return nums

📝 Problem Statement:
A company maintains a daily shift schedule for its employees, where each employee is assigned a fixed position in an array based on their order of work on Day 1.

To ensure fairness in work distribution, the company follows a policy where the schedule is adjusted every morning: the first d employees are moved to the end of the schedule, preserving their order.

You are given the list of employee IDs for Day 1 and the value d. Write a program to compute the new schedule after applying this policy.
Input:
schedule = [101, 102, 103, 104, 105]
d = 2

Output:
[103, 104, 105, 101, 102]

Explanation:
Employees 101 and 102 are shifted to the end of the schedule.
📝 Problem Statement:
A company maintains a daily shift schedule for its employees, where each employee is assigned a fixed position in an array based on their order of work on Day 1.

To ensure fairness in work distribution, the company follows a policy where the schedule is adjusted every morning: the first d employees are moved to the end of the schedule, preserving their order.

You are given the list of employee IDs for Day 1 and the value d. Write a program to compute the new schedule after applying this policy.
Input:
schedule = [101, 102, 103, 104, 105]
d = 2

Output:
[103, 104, 105, 101, 102]
'''
class em:
    def id(self,sch):
        n=len(sch)
        d=2
        temp=[0]*n
        for i in range(len(sch)):
            temp[(n-d+i)%n]=sch[i]
        for i in range(len(sch)):
            sch[i]=temp[i]
        return sch
sch=[101,102,103,104,105]                   
kk=em()
print(kk.id(sch))


