 class tree:
	def __init__(self,val):
		self.data=val
		self.left=None
		self.right=None
	def height(self,root):
		if root:
			q=[]
			h=1
			q.append(root)
			while q:
				count=	q.len()
				h+=1
				while count>0:
					temp=q.pop[0]
					if temp.left is not None:
						q.append(temp.left)
					if right.temp is not None:	
						q.append(temp.right)
					count-=1
		return h

if __name__=="__main__":
    root = tree(1)
    root.left = tree(2)
    root.right = tree(3)
    root.left.left = tree(4)
    root.left.right = tree(5) 
    print("Print height tree",root.height(root))
   