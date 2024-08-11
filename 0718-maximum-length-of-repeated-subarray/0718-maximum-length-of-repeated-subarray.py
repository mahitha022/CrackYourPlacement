class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp=[0]*(len(nums1))
        dp=[[0]*(len(nums2)) for i in range(len(dp))]
        
        m=0
        
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if(nums1[i]==nums2[j]):
                    if(i==0 or j==0):
                        dp[i][j]=1
                    else:
                        dp[i][j]=dp[i-1][j-1]+1
                    m=max(m,dp[i][j])
        
        
        return m