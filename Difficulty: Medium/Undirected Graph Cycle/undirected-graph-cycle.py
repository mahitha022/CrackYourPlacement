from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		
		def dfs(child,parent):
		    if(visit[child]==True):
		        return True
		    
		    visit[child]=True
		    for c in adj[child]:
		        if(c!=parent):
		            if(dfs(c,child)):
		                return True
		    return False
		
		
		visit=[False]*V
		for i in range(V):
		    if(visit[i]==False):
		        if(dfs(i,-1)):
		            return 1
		return 0
		        


#{ 
 # Driver Code Starts

if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends