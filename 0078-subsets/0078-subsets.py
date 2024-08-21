class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def back(i):
            if(i==len(nums)):
                res.append(tmp.copy())
                return
            
            tmp.append(nums[i])
            back(i+1)
            tmp.pop()
            back(i+1)
        
        res=[]
        tmp=[]
        back(0)
        return res