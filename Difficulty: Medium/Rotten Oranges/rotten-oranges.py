from  collections import deque

class Solution:

    #Function to find minimum time required to rot all oranges. 
	def orangesRotting(self, grid):
		#Code here
		
		q=deque()
		t=0
		f=0
		r=len(grid)
		c=len(grid[0])
		
		for i in range(r):
		    for j in range(c):
		        if(grid[i][j]==1):
		            f+=1
		        elif(grid[i][j]==2):
		            q.append([i,j])
		            
        directions=[[0,-1],[0,1],[1,0],[-1,0]]  
		 
		while(q and f>0):
		     
            for i in range(len(q)):
                a,b=q.popleft()
                
                for x,y in directions:
                    nx=x+a
                    ny=y+b
                    if(nx<0 or ny<0 or nx>=r or ny>=c or grid[nx][ny]!=1):
                        continue
                    f-=1
                    q.append([nx,ny])
                    grid[nx][ny]=2
            t+=1
        if(f==0):
            return t
        return -1


#{ 
 # Driver Code Starts
from queue import Queue


T=int(input())
for i in range(T):
	n, m = map(int, input().split())
	grid = []
	for _ in range(n):
		a = list(map(int, input().split()))
		grid.append(a)
	obj = Solution()
	ans = obj.orangesRotting(grid)
	print(ans)

# } Driver Code Ends