class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        r=len(matrix)
        c=len(matrix[0])
        dp=[0]*(r+1)
        dp=[[0]*(c+1) for i in range(r+1)]
        m=0
        for i in range(r):
            for j in range(c):
                if(matrix[i][j]>'0'):
                    
                    dp[i+1][j+1]=min(dp[i][j+1], dp[i][j], dp[i+1][j])+1
                    m=max(m,dp[i+1][j+1])
        
        #print(matrix)
        return m*m