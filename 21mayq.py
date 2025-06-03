class queue:
    def __init__(self,val,front,rear):
        self.Q=[]
        self.val=val
        self.front=-1
        self.rear=-1
    def enqueue(self,Q,val):
        if(self.front==-1):
            self.front=0
        self.rear+=1
        self.Q.append(val)
    def is_empty(self):
        if(self.front==-1):
            return "queue is empty"

    def dequeue(self,Q):
        if self.is_empty():
            return "queue is empty"
        val=self.queue[self.front]
        self.front+=1
        if self.front>self.rear:
            self.front=self.rear=-1
        return val

    def size(self):
        if self.is_empty():
            return 0
        return self.front-self.rear-1
    def display(self):
        if self.is_empty:
            "queue is empty"
        else:
            print(self.q[self.front:self.rear+1])
            
q=queue()
while True:
    print("1.Enqueue")
    print("2.Dequeue")
    print("3.isempty")
    print("4.size")
    print("5.exit")
    n=int(input("enter a number"))
    if n==1:
        q.enqueue()
    elif n==2:
        q.dequeue()
    elif n==3:
        q.is_empty()
    elif n==4:
        q.size()
    elif n==5:
        q.display()
    else:
        q.exit()
        
