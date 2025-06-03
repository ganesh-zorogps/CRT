class Node:
    def __init__(self,data):
        self.data=data
        self.next=None 
class LinkedList:
    def __init__(self):
        self.head=None       #starting point of linked list
    def insert_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            temp=self.head
            while temp.next:
                  temp=temp.next
            temp.next=new_node
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end="-->")
            temp=temp.next
        print("None")
    def add(self):
        temp=self.head
        sum=0
        while temp:
            sum=sum+temp.data
            temp=temp.next
        return sum
    def count(self):
        temp=self.head
        count=0
        while temp:
            temp=temp.next
            count+=1
        return count
    def insert_begin(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def dell(self):
        self.head=self.head.next
    def delen(self):
        temp=self.head
        while temp.next.next:
            temp=temp.next
        temp.next=None
    def ins_pos(self,pos,data):
        if(pos==0):
            self.insert_begin(data)
        else:
            new_node=Node(data)
            temp=self.head
            for i in range(pos-1):
                if temp is None:
                    print("positon out of bounds")
                    return
                temp=temp.next
            new_node.next=temp.next
            temp.next=new_node
    def delpo(self):
        if pos==0:
            self.dell()
        else:
            temp=self.head
            for _ in range(pos-1):
                 if temp.next is None:
                    print("out of bounds")
                    return
                 temp=temp.next
            temp.next=temp.next.next
    def del_val(self,value):
        if self.head.data==value:
            sef.head=self.head.next
            return
        temp=self.head
        while temp.next and temp.next.data!=value:
            temp=temp.next
        if temp.next is None:
            print("value not found")
            return
        temp.next=temp.next.next
ll=LinkedList()
ll.insert_end(10)
ll.insert_end(20)
ll.insert_end(30)
ll.insert_begin(40)
ll.dell()
ll.del_val(20)
ll.display()
print(f"sum of the elements is {ll.add()}")
print(f"count of the elements is {ll.count()}")
