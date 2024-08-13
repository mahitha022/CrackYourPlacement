class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        d={}
        for i in range(len(nums)):
            d[nums[i]]=d.get(nums[i],0)+1
        
        dupli=list(d.keys())
        dupli.sort()
        dp=[0]*len(dupli)

        dp[0]=dupli[0]*d[dupli[0]]

        for i in range(1,len(dupli)):
            if(dupli[i]-1==dupli[i-1]):
                if(i-2>=0 ):
                    dp[i]=dp[i-2]+dupli[i]*d[dupli[i]]
                    dp[i]=max(dp[i],dp[i-1])
                else:
                    dp[i]=max(dp[i-1], dupli[i]*d[dupli[i]])
            else:
                dp[i]=dp[i-1]+dupli[i]*d[dupli[i]]
                
                
        
        return dp[-1]