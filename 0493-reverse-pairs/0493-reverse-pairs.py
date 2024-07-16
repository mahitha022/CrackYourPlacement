class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge(s,e):
            if(s>=e):
                return 0
            m=(s+e)//2
            c= merge(s,m)+ merge(m+1,e)
            i=s
            j=m+1
            while(i<=m and j<=e):
                if(nums[i]>2*nums[j]):
                    c+=m-i+1
                    j+=1
                else:
                    i+=1
            nums[s:e+1]=sorted(nums[s:e+1])
            return c
        
        return merge(0, len(nums)-1)
        
        