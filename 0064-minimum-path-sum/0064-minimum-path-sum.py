class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        r=len(grid)
        c=len(grid[0])
        dp=[float('inf')]*(r+1)
        dp=[[float('inf')]*(c+1) for i in range(r+1)]
        dp[r][c-1]=0
        
        for i in range(r-1,-1,-1):
            for j in range(c-1,-1,-1):
                dp[i][j]=min(dp[i][j+1],dp[i+1][j])+grid[i][j]
        
        
        return dp[0][0]