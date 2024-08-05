class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d={}
        for i in range(len(nums2)):
            for j in range(i+1,len(nums2)):
                if(nums2[j]>nums2[i]):
                    d[nums2[i]]=nums2[j]
                    break
            d[nums2[i]]=d.get(nums2[i],-1)
        
        for i in range(len(nums1)):
            nums1[i]=d[nums1[i]]
        
        return nums1