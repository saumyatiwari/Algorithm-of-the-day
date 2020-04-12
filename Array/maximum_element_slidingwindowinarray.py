import collections
def maxwindow(nums, k):
	d = collections.deque()
	res = []
	for i, val in enumerate(nums):
		while d and val > nums[d[-1]]:
			d.pop()
			#if last value in deque is smaller than current value remove the element that are stored in deque
		d.append(i)
		# if element is out of window than pop that element from the  deque
		if d[0]==i-k:
			d.popleft()
		if i>=k-1: 
			#check if the current element reached at window size or more than it store the result
			res.append(nums[d[0]])
	return res
	
	
	
if __name__ == '__main__':
	
	k= int(input())
	nums=list(map(int,input().split()))
	print(maxwindow(nums,k))

