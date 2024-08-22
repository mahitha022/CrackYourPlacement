#User function Template for python3


class Solution:
    
    #Function to find the maximum number of cuts.
    def maximizeTheCuts(self,n,x,y,z):
        #code here
        
        def back(n):
            if(n<0):
                return float("-inf")
            if(n==0):
                return 0
            if(dp[n]==-1):
                
                cutx,cuty,cutz=float("-inf"),float("-inf"),float("-inf")
                if(n-x>=0):
                    cutx=back(n-x)+1
                if(n-y>=0):
                    cuty=back(n-y)+1
                if(n-z>=0):
                    cutz=back(n-z)+1
                dp[n]=max(cutx,cuty,cutz)
            
            return dp[n]
            
        dp=[-1]*(n+1)
        res= back(n)
        if(res<0):
            return 0
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    t=int(input())
    for tcs in range(t):
        n=int(input())
        x,y,z=[int(x) for x in input().split()]
        
        print(Solution().maximizeTheCuts(n,x,y,z))
# } Driver Code Ends