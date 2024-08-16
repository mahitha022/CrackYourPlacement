class Solution:
    def canCross(self, stones: List[int]) -> bool:
      
        
        def dfs(val,k):
            
            if((val,k) in s):
                return False
            
            if(val==target):
                return True
            
            if(val<0 or val>target or k<=0 or val not in stones):
                return False
            
            jump=[k-1,k,k+1]
            for j in jump:
                if(val+j in stones):
                    if(dfs(val+j,j)):
                        return True
                    
            s.add((val,k))
            return False
        
        s=set()
        target=stones[-1]
        stones=set(stones)
        
        return dfs(1,1)
        
        
