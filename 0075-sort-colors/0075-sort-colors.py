class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=[0,0,0]
        for i in nums:
            l[i]+=1
        c=0
        for i in range(len(l)):
            for j in range(l[i]):
                nums[c]=i
                c+=1
        