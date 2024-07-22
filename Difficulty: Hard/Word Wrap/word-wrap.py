#User function Template for python3

class Solution:
	def solveWordWrap(self, nums, k):
		#Code here
		def wrap(i,rem):
		    if(i==n):
		        return 0
		        
		    if(dp[i][rem]>-1):
		        return dp[i][rem]
		        
		    if(nums[i]>rem):
		        c=(rem+1)*(rem+1)+wrap(i+1,k-nums[i]-1)
		        
		    else:
		        op1=(rem+1)*(rem+1)+wrap(i+1,k-nums[i]-1)
		        op2=wrap(i+1,rem-nums[i]-1)
		        c=min(op1,op2)
		        
		    dp[i][rem]=c
		    return dp[i][rem]
		    
		    
		    
		    
		    
	    n=len(nums)
	    dp=[]
	    for i in range(n):
	        dp.append([-1]*(k+1))
	    return wrap(0,k)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		k = int(input())
		obj = Solution()
		ans = obj.solveWordWrap(nums, k)
		print(ans)


# } Driver Code Ends