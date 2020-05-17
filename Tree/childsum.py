class Node: 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None

  
def childsum(root): 
    left_dt=0
    right_dt=0
    # Base condition 

    if (root is None or (root.left is None and root.right is None)): 
        return True
    if(root.left):
        left_dt=root.left.data 
    if(root.right):
        right_dt=root.right.data    

    if (root.data==left_dt+right_dt and childsum(root.left) is True and childsum(root.right) is True): 
        return True
  
    return False

   
root = Node(10)  
root.left = Node(8)  
root.right = Node(2)  
root.left.left= Node(3)  
root.left.right = Node(5)  
root.right.right = Node(2) 
if childsum(root): 
    print("Tree satisies the Childsum property") 
else:
    print("Tree doesn't satisies the Childsum property") 
  