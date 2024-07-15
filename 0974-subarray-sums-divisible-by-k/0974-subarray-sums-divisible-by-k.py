class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d={0:1}
        c=0
        s=0
        for i in range(len(nums)):
            s+=nums[i]
            divi=s%k
            if(divi in d):
                c+=d[divi]
                d[divi]+=1
            else:
                d[divi]=1
        return c