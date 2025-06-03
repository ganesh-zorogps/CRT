stack=[]
top=-1
def push(val):
    global top
    stack.append(val)
    top+=1
def pop():
    global top
    if top==-1:
        print("stack is empty nothing to pop")
        return
    else:
        stack.pop()
        top-=1
def peak():
    if top==-1:
        return "stack is empty no top element"
    else:
        return f"the peak element is {stack[top]}"
def display():
    if(pop==-1):
        print("stack is empty")
    else:
        for i in range(top,-1,-1):
            print(stack[i])
def exit():
    return exit
while True:
    print("1.push")
    print("2.pop")
    print("3.peak")
    print("4.display")
    print("5.exit")
    n=int(input("enter a number"))
    if n==1:
       el=int(input("enter the element to push"))
       print(stack.append(el))
    elif n==2:
       pop()
    elif n==3:
       peak()
    elif n==4:
       display()
    else:
       exit()
    break


