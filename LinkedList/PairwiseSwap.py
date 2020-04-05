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
		print("")	

	def pairwiseswap(self):
		if self.head is None:
			return 
		temp=self.head
		while temp is not None and 	temp.next is not None :
			temp.data,temp.next.data=temp.next.data,temp.data
			temp=temp.next.next

def main():
    print("Enter Linked list elements: ")
    l1=linkedlist()
    arr=[int(x) for x in input().strip().split()]
    for num in arr:
        l1.push(num)
    
    print("Entered Linked List is: ")
    l1.print_linkedlist()
    l1.pairwiseswap()
    print("Swapped list is: ")
    l1.print_linkedlist()

if __name__=="__main__":
    main()	
