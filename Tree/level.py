 class tree:
	def __init__(self,val):
		self.data=val
		self.left=None
		self.right=None
	def level(self,root):
		if root:
			q=[]
			q.append(root)
			while q:
				count=	q.len()
				while count>0:
					temp=q.pop[0]
					print(temp,end="")
					q.append(temp.left)
					q.append(temp.right)
					count-=1
			print("")		 
if __name__=="__main__":
    root = tree(1)
    root.left = tree(2)
    root.right = tree(3)
    root.left.left = tree(4)
    root.left.right = tree(5)

    print("level Traversal (): ")
    root.level(root)
   