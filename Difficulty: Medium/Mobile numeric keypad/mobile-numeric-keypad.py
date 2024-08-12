#User function Template for python3
class Solution:
	def getCount(self, n):
		# code here
		if(n==1):
		    return 10
		jump=[[0,8],[1,2,4],[1,2,3,5],[2,3,6],[1,4,5,7],[2,4,5,6,8],[3,5,6,9],[4,7,8],[0,7,8,5,9],[6,8,9]]
		
		dp=[1]*10
		
		for _ in range(n-1):
		    temp=[0]*10
		    for i in range(10):
		        for j in jump[i]:
		            temp[j]+=dp[i]
		    dp=temp
		return sum(dp)
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        ob = Solution()
        ans = ob.getCount(n)
        print(ans)

# } Driver Code Ends