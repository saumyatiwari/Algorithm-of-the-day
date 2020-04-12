#code
def areainhistogram(A, l):
	area=0
	for i in range(1,n-1):
		left=A[i]
		for j in range(0,i):
			left=max(left,A[j]) #Get the max area from left and right so that at given location we can find trapped water
		for j in range(i+1,n):
			right=max(right,A[j])
		area=min(left,right)-A[i]
    return A[i]		
	
	
if __name__=="__main__": 
	n=int(input())
	while n>0:
		n=n-1
		#print(n)
		l=int(input())
		
		A =list(map(int,input().split()))
		
		 
		print("areainhistogram(A, l)")
