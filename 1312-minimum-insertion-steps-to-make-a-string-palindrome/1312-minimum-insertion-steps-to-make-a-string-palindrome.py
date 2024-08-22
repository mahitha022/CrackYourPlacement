class Solution:
    def minInsertions(self, s: str) -> int:
        
        def longestpalinsubseq(s):
            revs=s[::-1]
            n=len(s)
            m=len(revs)
            dp=[[0]*(n+1) for i in range(m+1)]
            
            for i in range(n):
                for j in range(m):
                    if(s[i]==revs[j]):
                        dp[i+1][j+1]=1+dp[i][j]
                    else:
                        dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j])
            return dp[n][m]
        
        
        res=longestpalinsubseq(s)
        return len(s)-res