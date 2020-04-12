#2 stack 1 array
class twostack:
    def __init__(self,k,n):
        self.n=n
        self.k=k
        self.top=[-1]*self.k
        self.arr=[0]*self.n
        self.top[0]=0
        self.top[1]=n-1
    def insert(self,val,sn):
        	if self.top[0]<self.top[1] and sn==0:
        		self.arr[self.top[sn]]=val
        		self.top[sn]+=1
        	else:
        		if(self.top[0]<self.top[1] and sn==1):
        			self.arr[self.top[sn]]=val
        			self.top[sn]-=1
        		else:
        			print("Overflow")		
    def remove(self,sn):
    		if sn==0 and int(self.top[sn])>=0:
    			self.arr[self.top[sn]]=0
    			self.top[sn]-=1
    		else:
    			print("Underflow")
    		if sn==1 and int(self.top[sn])<=n-1:
    			self.arr[top[sn]]=0
    			self.top[sn]+=1
    		else:
    			print("Underflow")	
    def printarray(self):
    		for i in self.arr:
    			print(i,end=" ");



def main():
	print("Enter the array size")
	sz=int(input())
	st=twostack(2,sz)
	while True:
		print("Press1 to insert in 1 array")
		print("Press2 to pop from  1 array")
		print("Press3 to insert in 2 array")
		print("Press4 to pop from 2 array")
		print("Press 5 to exit") 
	
		i=int(input())

		if(i==1):
			n=int(input())
			st.insert(n,0)
			st.printarray()
		if(i==2):
			print("element will get removed from 1 stack ")
			st.remove(0)
			st.printarray()
		if(i==3):
			n=int(input())
			st.insert(n,1)
			st.printarray()
		if(i==4):
			print("element will get removed from 2 stack ")
			st.remove(1)
			st.printarray()	
		if(i==5):
		  	return	


if __name__ == '__main__':
    main()