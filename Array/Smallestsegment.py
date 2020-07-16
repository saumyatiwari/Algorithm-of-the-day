def smallestSubsegment(arr, l):
	left=dict()
	count=dict()
	mx=0
	mn,strtindex=0,0
	print(mn, end=" ")
	for i in range(n):
		x=arr[i]
		if(x not in count.key()):
			left[x]=i
			count[x]=1
		else: 
			count[x]+=1
		if(count[x]>mx):
			mx=count[x]
			mn=i-left[x]+1
			strtindex=left[x]	
		elif(cout[x]==mx and mn<i-left[x]+1):
		    mn=i-left+1
		    strtindex=left[x]
	for i in (strtindex,strtindex+mn):
	    print(arr[i],end=" ")	    



def main():
	t=int(input())
	for k in range(t):
	    n=int(input())
	    arr=[int(x) for x in input().strip().split()]
	    smallestSubsegment(arr, l) 
		
