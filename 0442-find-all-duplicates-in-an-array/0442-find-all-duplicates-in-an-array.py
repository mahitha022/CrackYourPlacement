class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d={}
        l=[]
        for i in nums:
            d[i]=d.get(i,0)+1
            if(d[i]>1):
                l.append(i)
        return l
        