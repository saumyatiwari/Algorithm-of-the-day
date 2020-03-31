# your task is to complete this function
# function should return index to the any valid peak element
def findMid(head):
    # Code here

    slow = head
    fast = head
    # print(head.data)
    while( temp_fast.next &temp_fast.next.next):
        # print(temp_slow.data,temp_fast.data)
        temp_slow = temp_slow.next
        #temp = temp_fast.next
        temp_fast = temp_fast.next.next
    # print(temp_slow.data,temp_fast.data)
    
    if not(temp_fast.next):
        return temp_slow
    else:
        return temp_slow.next



        




#{ 
#  Driver Code Starts
# Node Class    
class node:
    def __init__(self, val):
        self.data = val
        self.next = None
        
# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None

    def insert(self, val):
        if self.head == None:
            self.head = node(val)
        else:
            new_node = node(val)
            temp = self.head
            while(temp.next):
                temp=temp.next
            temp.next = new_node

def createList(arr, n):
    lis = Linked_List()
    for i in range(n):
        lis.insert(arr[i])
    return lis.head

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        head = createList(arr, n)
        print(findMid(head).data)




# } Driver Code Ends