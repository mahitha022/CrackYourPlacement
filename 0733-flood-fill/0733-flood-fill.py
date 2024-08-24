class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        def dfs(i,j):
            if(i<0 or j<0 or i>=n or j>=m or visit[i][j]):
                return 
            if(image[i][j]==target):
                visit[i][j]=True
                image[i][j]=color
                for x,y in d:
                    nx,ny=i+x,j+y
                    dfs(nx,ny)
                
        n=len(image)
        m=len(image[0])
        d=[[-1,0],[0,-1],[1,0],[0,1]]
        target=image[sr][sc]
        
        visit=[[False]*m for i in range(n)]
        dfs(sr,sc)
        #image[sr][sc]=color
        return image