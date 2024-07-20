class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        heapq.heapify(nums)
        lar=heapq.nlargest(3,nums)
        smol=heapq.nsmallest(2,nums)
        return max(lar[0]*lar[1]*lar[2], smol[0]*smol[1]*lar[0])
        #nums.sort(reverse=True)
        #return max(nums[0]*nums[1]*nums[2], nums[-1]*nums[-2]*nums[0])
        