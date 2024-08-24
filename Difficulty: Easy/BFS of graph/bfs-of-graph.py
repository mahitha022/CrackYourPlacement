#User function Template for python3

from typing import List
from queue import Queue
from collections import deque
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        # code here
        q=deque()
        visit=[0]*V
        q.append(0)
        res=[]
        
        while(q):
            node=q.popleft()
            if(visit[node]==0):
                visit[node]=1
                res.append(node)
            
            child=adj[node]
            for c in child:
                if(visit[c]==0):
                    q.append(c)
        return res


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
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends