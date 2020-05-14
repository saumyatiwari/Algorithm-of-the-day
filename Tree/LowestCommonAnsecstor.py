 class tree:
	def __init__(self,val):
		self.data=val
		self.left=None
		self.right=None
def FindLCA(root,n1,n2):
		if root is None:
			return None
		if root.data==n1 or root.data==n2:
			return root	
		left_lca=FindLCA(root->left,n1,n2)	
		right_lca=FindLCA(root->right,n1,n2)
		if root.data==n1 or root.data==n2:
			return root
		if left_lca and right_lca:
			return root
		return left_lca if left_lca is not None else right_lca

if __name__=="__main__":
    root = tree(1)
    root.left = tree(2)
    root.right = tree(3)
    root.left.left = tree(4)
    root.left.right = tree(5) 
    n1,n2=int(input())
    print("Lowest Common Ansestor",FindLCA(root,n1,n1).data)
   