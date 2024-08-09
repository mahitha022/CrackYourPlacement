class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cmax=1
        cmin=1
        res=float('-inf')
        for i in nums:
            if(i==0):
                cmax=1
                cmin=1
            
            tmp=cmax*i
            
            cmax=max(tmp,cmin*i,i)
            cmin=min(tmp,cmin*i,i)
            res=max(res,cmax)
        
        return res