def maxDiff(arr, arr_size): 
    max_diff = arr[1] - arr[0] 
    min_element = arr[0] 
      
    for i in range( 1, arr_size ): 
        if (arr[i] - min_element > max_diff): 
            max_diff = arr[i] - min_element 
      
        if (arr[i] < min_element): 
            min_element = arr[i] 
    return max_diff 

	
if __name__ =='__main__':
	
	k= int(input())
	nums=list(map(int,input().split()))
	print(maxDiff(nums,k))
      