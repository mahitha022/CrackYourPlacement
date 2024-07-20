#User function Template for python3

class Solution:
    def productExceptSelf(self, nums, n):
        #code here
        n=len(nums)
        l=[1]*n
        for i in range(1,n):
            l[i]=nums[i-1]*l[i-1]
        c=nums[-1]
        for i in range(n-2,-1,-1):
            l[i]=c*l[i]
            c=c*nums[i]
            
            
        return l


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())

    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]

        ans=Solution().productExceptSelf(arr,n)
        print(*ans)
# } Driver Code Ends