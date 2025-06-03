class Node:
    def __init__(self,prv,next,data):
        self.prv=None
        self.next=None
        self.data=data
class DoublyLinkedList:
    def __init__(self):
        self.head=None
    def insert_begin(self,data):
        new_node=Node(None,None,data)
        if self.head is None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head.prv=new_node
            self.head=new_node
    def del_begin(self):
        self.head=self.head.next
        self.head.prv=None
    def del_end(self):
        if self.head.next is None:
            self.head = None
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.prv.next=None
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end="-->")
            temp=temp.next
        print("None")

dll=DoublyLinkedList()
dll.insert_begin(10)
dll.insert_begin(20)
dll.insert_begin(30)
dll.insert_begin(40)
dll.del_begin()
dll.del_end()
dll.display()
