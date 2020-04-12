#code
def stockBuySell(A, l):
	f=0
	l=len(A)
	if l<=1:
		print("No Profit")
	for i in range(0,l-1):
		if A[i]<A[i+1]:
			index_buy=i
			#buy the stock when price is lowest
			index_sell=i+1
			if(l<l):
			    i=i+1
			while A[index_sell]<A[i+1] and i+1<l:
				index_sell=i+1
				#increase the selling price til it reaches the maximum value
				if(i<l):
				    i=i+1
			        
			if index_buy<index_sell:
				print("("+str(index_buy)+" "+str(index_sell)+")",end=" ")
				f=1
		else:
		    continue
	if f==0:
		print("No Profit")
		
		
if __name__=="__main__": 
	n=int(input())
	while n>0:
		n=n-1
		#print(n)
		l=int(input())
		
		A =list(map(int,input().split()))
		
		stockBuySell(A, l) 
		print("")
   
        
                
            



                
    
    
        
