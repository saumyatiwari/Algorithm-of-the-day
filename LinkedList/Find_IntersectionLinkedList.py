class Node:
	def __init__(self,data):
		self.data=data
		self.next=None

class Linkedlist:
	def __init__(self):
		self.head=None
	def push(self,data):
		new_node = Node(data)
		if self.head is None:
			self.head=new_node
			return
		temp =self.head
		while temp.next is not None:
			temp=temp.next
		temp.next=new_node
		return
	def printlist(self):
		if self.head is None:
			return
		temp=self.head
		while temp:
			print(temp.data,end="")
			temp=temp.next
		print("")
	def intersection(self,head_b):
		
		list_a=self.head
		list_b=head_b
		x=0
		y=0
		while list_a:
			x+=1
			
			list_a=list_a.next
		while list_b:
		 	y+=1
		 	
		 	list_b=list_b.next
		list_a=self.head
		list_b=head_b
		if x>y:
			diff=x-y
			while diff:
				
				list_a=list_a.next
				diff-=1

		else:
			diff=y-x
			while diff:
				
				list_b=list_b.next
				diff-=1		
		while list_a and list_b:
		
			list_a=list_a.next
			list_b=list_b.next
			if list_a.data==list_b.data:
				return list_a.data
		return -1	




def main():
	print("Enter 1st Linkedlist element")
	l1=Linkedlist()
	arr=[int(x) for x in input().strip().split()]				 		
	for num in arr:
		l1.push(num)
	print("1st list")
	l1.printlist()	
	print("Enter 2st Linkedlist element")
	l2=Linkedlist()
	arr=[int(x) for x in input().strip().split()]				 		
	for num in arr:
		l2.push(num)	
	print("2st list")
	l2.printlist()	
	if l1.intersection(l2.head)== None:
		print(-1)
	else:
		print(l1.intersection(l2.head))	
if __name__ == "__main__":
	main()			
