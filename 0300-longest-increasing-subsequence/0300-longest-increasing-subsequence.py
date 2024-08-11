class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp=[1]*len(nums)
        
        
        for i in range(len(nums)-2,-1,-1):
            m=0
            for j in range(i,len(nums)):
                if(nums[i]<nums[j]):
                    m=max(m,dp[j])
            dp[i]+=m
        
        return max(dp)