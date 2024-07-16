class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        m=n/2
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
            if(d[i]>m):
                return i
        