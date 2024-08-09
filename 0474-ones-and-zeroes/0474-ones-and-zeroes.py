class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        def dfs(i,m,n):
            if(i==len(strs)):
                return 0
            if((i,m,n) in d):
                return d[(i,m,n)]
            
            d[(i,m,n)]=dfs(i+1,m,n)
            
            mcount=strs[i].count('0')
            ncount=strs[i].count('1')
            if(mcount<=m and ncount<=n):
                d[(i,m,n)]=max( dfs(i+1,m-mcount, n-ncount)+1, d[(i,m,n)])
            
            return d[(i,m,n)]
        
        d={}
        return dfs(0,m,n)