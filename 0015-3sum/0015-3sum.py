class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l=[]
        n=len(nums)
        for first in range(n-2):
            a=nums[first]
            if(first>0 and a==nums[first-1]):
                continue
            i=first+1
            j=n-1
            
            while(i<j):
                s=a+nums[i]+nums[j]
                if(s==0):
                    l.append([a,nums[i],nums[j]])
                    i+=1
                    while(nums[i]==nums[i-1] and i<j):
                        i+=1
                elif(s<0):
                    i+=1
                else:
                    j-=1
        return l
