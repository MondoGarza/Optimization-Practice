class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 
  
  
# A function to do inorder tree traversal 
def printInorder(root): 
    if root: 
        printInorder(root.left) 
        print(root.val), 
        printInorder(root.right) 
  
def printPostorder(root): 
  
    if root: 
        printPostorder(root.left) 
        printPostorder(root.right) 
        print(root.val),


def printPreorder(root): 
  
    if root: 
        print(root.val), 
        printPreorder(root.left)  
        printPreorder(root.right)
        

# Driver code 
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5)
root.left.left.left = Node(10)
root.left.left.right = Node(11) 

print("Preorder traversal:")
printPreorder(root) 
  
print("\nInorder traversal:")
printInorder(root) 

print("\nPostorder traversal:")
printPostorder(root)  