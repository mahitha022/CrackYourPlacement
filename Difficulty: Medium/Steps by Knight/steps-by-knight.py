from collections import deque
class Solution:

	#Function to find out minimum steps Knight needs to reach target position.
	def minStepToReachTarget(self, KnightPos, TargetPos, N):
		#Code here
		
		def check(i,j):
		    if(i<0 or j<0 or i>=N or j>=N or visit[i][j]):
		        return False
		    return True
		
		d=[[-1,-2],[-1,2],[1,-2],[1,2],[2,1],[2,-1],[-2,1],[-2,-1]]
		targeti=TargetPos[0]-1
		targetj=TargetPos[1]-1
		i=KnightPos[0]-1
		j=KnightPos[1]-1
		q=deque()
		visit=[[False]*N for i in range(N)]
		q.append([0,i,j])
		visit[i][j]=True
		while(q):
		    cost,i,j=q.popleft()
		    if(i==targeti and j==targetj):
		        return cost
		    for x,y in d:
		        nx,ny=x+i,y+j
		        if(check(nx,ny)):
		            q.append([cost+1,nx,ny])
		            visit[nx][ny]=True


#{ 
 # Driver Code Starts

T=int(input())
for i in range(T):
	N = int(input())
	KnightPos = list(map(int, input().split()))
	TargetPos = list(map(int, input().split()))
	obj = Solution()
	ans = obj.minStepToReachTarget(KnightPos, TargetPos, N)
	print(ans)

# } Driver Code Ends