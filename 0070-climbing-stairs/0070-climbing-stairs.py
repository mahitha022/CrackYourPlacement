class Solution:
    def climbStairs(self, n: int) -> int:
        
        def back(n):
            if(n==0 or n==1):
                return 1
            if(n not in d):
                
                d[n]=back(n-1)+back(n-2)
                
            return d[n]
        
        d={}
        return back(n)