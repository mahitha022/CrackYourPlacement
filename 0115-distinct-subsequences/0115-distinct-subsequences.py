class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        def dfs(i,j):
            
            # s="a" t=""
            if(j==len(t)):
                return 1
            
            #s="" t="a"
            if(i==len(s)):
                return 0
            
            if((i,j) in d):
                return d[i,j]
            
            if(s[i]==t[j]):
                d[i,j]= dfs(i+1,j+1)+dfs(i+1,j)
            
            else:
                d[i,j]=dfs(i+1,j)
                
            return d[i,j]
            
            
            
        d={}
        return dfs(0,0)