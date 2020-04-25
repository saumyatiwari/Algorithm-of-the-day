def lenOfLongSubarr(arr, n, k): 

    mydict = dict() 
      sum = 0
    maxLen = 0
  
    for i in range(n): 
  
        # accumulate the sum 
        sum += arr[i] 
  
        if (sum == k): 
            maxLen = i + 1
  
   
        elif (sum - k) in mydict: 
            maxLen = max(maxLen, i - mydict[sum - k]) 
  
        if sum not in mydict: 
            mydict[sum] = i 
  
    return maxLen 

def main():
	print("Enter the element in array")
	arr=[int(x) for x in input().strip().split()]
	n=len(arr)
	print("Enter the sum value")
	k=int(input())
	print("Lenght=",lenOfLongSubarr(arr, n, k))
if __name__=="__main__":
    main()


