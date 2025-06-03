'''
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class bst:
    def __init_(self):
        self.root=None
    def insert(self,data,root):
        if root is None:
            return Node(data)
        if data<root.data :
            root.left=self.insert(data,root.left)
        elif data>root.data:
            root.right=self.insert(data,root.right)
        return root
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data,end=" ")
            self.inorder(root.right)
        
    def preorder(self,root):
        if root:
            print(root.data,end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data,end=" ")
    def search(self,root,key):
        if root==key:
            return True
        if root is None:
            return False
        if key<root.data:
            return self.search(root.left,key)
        elif key>root.data:
            return self.search(root.right,key)
        else:
            return True
    def height(self,root):
        if root is None:
            return 0
        return max(self.height(root.left),self.height(root.right))+1
            

bstree=bst()
root=None
root=bstree.insert(20,root)
root=bstree.insert(16,root)
root=bstree.insert(50,root)
root=bstree.insert(60,root)
root=bstree.insert(500,root)
print(root.data)
print(bstree.search(root,20))
print(bstree.height(root))

bstree.postorder(root)
bstree.preorder(root)
bstree.inorder(root)
'''


    
    
    


