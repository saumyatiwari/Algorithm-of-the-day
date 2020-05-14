class tree:
	def __init__(self,val):
		self.data=val
		self.left=None
		self.right=None
	def inorder(self,root):
		if root:
			self.inorder(root.left)
			print(root.data,end=" ")
			self.inorder(root.right)
		else:
			return	
	def post(self,root):
		if root:
					
			self.post(root.left)
			self.post(root.right)
			print(root.data,end=" ")
		else:
			return		
	def preorder(self,root):
		if root:
			print(root.data,end=" ")
			self.preorder(root.left)
			self.preorder(root.right)
		else:
			return	
if __name__=="__main__":
    root = tree(1)
    root.left = tree(2)
    root.right = tree(3)
    root.left.left = tree(4)
    root.left.right = tree(5)

    print("Preorder Traversal (): ")
    root.preorder(root)
    print("")
    print("Postorder Traversal (): ")
    root.post(root)
    print("")
    print("Inorder Traversal (): ")
    root.inorder(root)
    print("")