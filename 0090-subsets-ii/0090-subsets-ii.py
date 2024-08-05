class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def dtree(i,sub):
            if(i==len(nums)):
                l.append(sub.copy())
                return
            sub.append(nums[i])
            dtree(i+1,sub)
            sub.pop()
            
            while(i+1<len(nums) and nums[i]==nums[i+1]):
                i+=1
            
            dtree(i+1,sub)
        
        l=[]
        nums.sort()
        dtree(0,[])
        return l