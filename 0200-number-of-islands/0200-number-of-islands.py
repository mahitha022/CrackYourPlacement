class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(i,j):
            if(i<0 or j<0 or i>=n or j>=m or grid[i][j]=='0'):
                return False
            
            grid[i][j]='0'
            for x,y in d:
                nx,ny=i+x,j+y
                dfs(nx,ny)
        
        
        
        
        d=[[0,0],[-1,0],[0,-1],[1,0],[0,1]]
        n=len(grid)
        m=len(grid[0])
        c=0
        for i in range(n):
            for j in range(m):
                if(grid[i][j]=='1'):
                    c+=1
                    dfs(i,j)
        return c