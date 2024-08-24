#User function Template for python3
from typing import List

class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V : int , adj : List[List[int]]) -> bool :
        # code here
        
        def dfs(i):
            if(visit[i]==True):
                return True
            visit[i]=True
            dfsvisit[i]=True
            for c in adj[i]:
                if(visit[c]==False):
                    if(dfs(c)):
                        return True
                elif(dfsvisit[c]==True):
                    return True
                    
            dfsvisit[i]=False
            return False
        
        
        visit=[False]*V
        dfsvisit=[False]*V
        for i in range(V):
            if(visit[i]==False):
                if(dfs(i)):
                    return 1
        return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V, E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a, b = map(int, input().strip().split())
            adj[a].append(b)
        ob = Solution()

        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)

# } Driver Code Ends