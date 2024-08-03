class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        def dfs(i,j):
            if((i,j) in d):
                return d[(i,j)]
            
            if(i>=j):
                return 0
            else:
                res=float('inf')
                for k in range(i,j):
                    value=max(arr[i:k+1])*max(arr[k+1:j+1])
                    res=min(res, dfs(i,k)+dfs(k+1,j)+value)
                d[(i,j)]=res
            return d[(i,j)]
        
        
        
        
        d={}
        return dfs(0,len(arr)-1)