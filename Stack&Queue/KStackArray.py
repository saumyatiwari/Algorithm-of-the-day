#2 stack 1 array
class twostack:
    def __init__(self,k,n):
        self.n=n
        self.k=k
        self.top=[-1]*self.k
        self.arr=[0]*self.n
        self.next=[i for i in range(1,self.n)]
        self.next.append(-1)
        # Top of the free stack. 
        self.free = 0
           # Check whether given stack is empty. 
    def isEmpty(self, sn): 
        return self.top[sn] == -1
  
    # Check whether there is space left for  
    # pushing new elements or not. 
    def isFull(self): 
        return self.free == -1


    def insert(self,val,sn):
        if (self.isFull()):
            print("stackoverflow")
        i=self.free
        self.free=self.next[i]  
        self.arr[i]=val
        self.next[i]=self.top[sn]
        self.top[sn]=i        
    def remove(self,sn):
        if self.isEmpty(sn): 
            return None
        top_stack=self.top[sn]
        self.top[sn]=self.next[self.top[sn]]
        self.next[top_stack]=self.free 
        self.free=top_stack 
        for i in self.next:
                print(i,end=" ");
        return self.arr[top_stack]

    def printarray(self):
    		for i in self.arr:
    			print(i,end=" ");
            



def main():
    print("Enter the array size")
    sz=int(input())
    print("Enter the number of linked list you want to implement")
    k=int(input())
    st=twostack(k,sz)
    while True:
        print("Press1 to insert in  array")
        print("Press2 to pop from  array")
        print("Press3 to exit")
        i=int(input())
        if(i==1):
            print("Enter element and stack no in which u want to insert")
            n=int(input())
            k=int(input())
            st.insert(n,k-1)
            st.printarray()
        if(i==2):
            print("Enter stack no from which u want to remove")
            k=int(input())
            print(st.remove(k-1))
            st.printarray()
        if(i==3):
            return	


if __name__ == '__main__':
    main()