class Node:
	def __init__(self,data):
		self.data=data
		self.next=None

class linkedlist:

	def __init__(self):
		self.head=None

	def push(self,data):
		new_node=Node(data)

		if self.head is None:
			self.head=new_node
			return

		temp=self.head
		while temp.next is not None: 
			temp=temp.next
		temp.next=new_node
		return

	def print_linkedlist(self):
		if self.head is None:
			return 

		temp=self.head
		while temp:
			print(temp.data,end=" ")
			temp=temp.next
		print ("")	
	def recursive_rev(self,node):
		if(node.next==None):
			self.head=node
			return 
		self.recursive_rev(node.next)
		# 1,2,3,4 suppose it reaches to 3 then it will pass 4 
		# node.next.next 3rd node address.next.next hence the last pointer node start pointing to 3 and 3 rd node next will become null 
		
		node.next.next=node
		node.next=None		

def main():
    print("Enter Linked list elements: ")
    l1=linkedlist()
    arr=[int(x) for x in input().strip().split()]
    for num in arr:
        l1.push(num)
    
    print("Entered Linked List is: ")
    l1.print_linkedlist()
    l1.recursive_rev(l1.head)
    print("Reversed list is: ")
    l1.print_linkedlist()

if __name__=="__main__":
    main()
