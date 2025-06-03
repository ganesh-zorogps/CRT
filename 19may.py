p=input("enter the password")
score=0
if any(i.islower for i in p)and any(i.isupper for i in p):
    score=6
if any(i.isdigit for i in p):
    score=8
if any(i in "!@#$%^&*()_=[]{}:;/?><|\.," for i in p):
    score=10
if 6>=score<7:
    print("password is weak")
if 8>=score<9:
    print("password is strong")
if score==10:
    print("password is very strong")
