#Count distinct elements in an array

def distinctele(arr,n):	
	s=set()
	res=0
	for i in range(n):
		if (arr[i] not in s):
			 s.add(arr[i])
			 res+=1
	print(res)
	

def main():
    print("Enter Linked list elements: ")
    arr=[int(x) for x in input().strip().split()]
    n = len(arr)
    print(distinctele(arr,n))
if __name__=="__main__":
    main()	