class Node:
    def __init__(self):
        self.data=None
        self.left=None
        self.right=None
    def inorder_traversal(self,Node):
        if Node:
            self.inorder_traversal(Node.left)
            print(Node.data,end=" ")
            self.inorder_traversal(Node.right)
    def preorder_traversal(self,Node):
        if Node:
            print(Node.data,end=" ")
            self.preorder_traversal(Node.left)
            self.preorder_traversal(Node.right)
    def postorder_traversal(self,Node):
        if Node:
            self.postorder_traversal(Node.left)
            self.postorder_traversal(Node.right)
            print(Node.data,end=" ")
    def sum(self,Node):
        if Node is None:
            return 0
        else:
            return Node.data+self.sum(Node.left)+self.sum(Node.right)
    def count(self,Node):
        if Node is None:
            return 0
        return 1+self.count(Node.left)+self.count(Node.right)
    def count_leaf(self,Node):
        if Node.left==Node.right==None:
            return self.count_leaf(Node.left)+self.count_leaf(Node.right)
    def height(self,Node):
        if Node is None:
            return 0
        else:
            return max(self.height(Node.left),self.height(Node.right))+1
tree=Node()
tree.data=1
tree.left=Node()
tree.left.data=2
tree.right=Node()
tree.right.data=3
tree.left.left=Node()
tree.left.left.data=4
tree.left.right=Node()
tree.left.right.data=5
tree.right.left=Node()
tree.right.left.data=6
tree.right.right=Node()
tree.right.right.data=7
print(tree.height(Node=tree))
'''
print(tree.count_leaf(Node=tree))
print(tree.count(Node=tree))
print(tree.count(Node=tree.left))
print(tree.count(Node=tree.right))


print(tree.sum(Node=tree))
print(tree.sum(Node=tree.left))
print(tree.sum(Node=tree.right))

tree.inorder_traversal(Node=tree)
tree.preorder_traversal(Node=tree)
tree.postorder_traversal(Node=tree)
'''
