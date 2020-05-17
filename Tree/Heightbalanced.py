class Node: 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None
  
def height(root): 
      
    # base condition when binary tree is empty 
    if root is None: 
        return 0
    return max(height(root.left), height(root.right)) + 1
  
def isBalanced(root): 
      
    # Base condition 
    if root is None: 
        return True
  
    # for left and right subtree height 
    lh = height(root.left) 
    rh = height(root.right) 
  
    # allowed values for (lh - rh) are 1, -1, 0 
    if (abs(lh - rh) <= 1) and isBalanced( 
    root.left) is True and isBalanced( root.right) is True: 
        return True
  
   
    return False
  
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.left.left.left = Node(8) 
if isBalanced(root): 
    print("Tree is balanced") 
else: 
    print("Tree is not balanced") 
  