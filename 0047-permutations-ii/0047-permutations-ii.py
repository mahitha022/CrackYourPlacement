class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        def back(ind,tmp):
            if(len(tmp)==n):
                s="_".join(map(str,tmp))
                if(s not in per):
                    per.add(s)
                    result.append(tmp.copy())
                return
                    
            
            for i in range(n):
                if(visit[i]==False):
                    visit[i]=True
                    tmp.append(nums[i])
                    back(i+1,tmp)
                    tmp.pop()
                    visit[i]=False
            
            
        visit=[False]*len(nums)
        per=set()
        n=len(nums)
        result=[]
        back(0,[])
        return result
        