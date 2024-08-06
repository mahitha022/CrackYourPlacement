class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def back(i,sums,sub):
            if(sums==target):
                s.add(tuple(sub))
                return
            if(i==n or sums>target):
                return
            
            back(i+1,sums+candidates[i],sub+[candidates[i]])
            
            while(i+1<n and candidates[i]==candidates[i+1]):
                i+=1
            back(i+1,sums,sub)
        
        
        candidates.sort()
        s=set()
        n=len(candidates)
        back(0,0,[])
        return list(s)