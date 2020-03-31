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

	def Segregate(self):
		if self.head is None:
			return 
		evenl1=linkedlist()
		oddl1=linkedlist()
		temp=self.head
		if temp.data%2==0:
			evenl1.push(temp.data)
		else:
			oddl1.push(temp.data)
		
		result=evenl1.head
		while result.next:
			result=result.next
		result.next=oddl1.head
		return evenl1	
				

def main():
    print("Enter Linked list elements: ")
    l1=linkedlist()
    arr=[int(x) for x in input().strip().split()]
    for num in arr:
        l1.push(num)
    
    print("Entered Linked List is: ")
    l1.print_linkedlist()
    l1.Segregate()
    print("Segregate list is: ")
    l1.print_linkedlist()

if __name__=="__main__":
    main()	
