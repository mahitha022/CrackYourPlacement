class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        if(n%2==0):
            med=(nums[n//2]+nums[(n//2)-1])//2
        else:
            med=nums[n//2]
        c=0
        for i in nums:
            c+=abs(med-i)
        return c
        