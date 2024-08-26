class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        def dfs(d,node):
            visit[node]=True
            for con in d[node]:
                if(visit[con]==False):
                    dfs(d,con)
        
        if(len(connections)<n-1):
            return -1
        d={}
        for i in range(n):
            d[i]=[]
        for i,j in connections:
            d[i].append(j)
            d[j].append(i)
        
        c=0
        visit=[False]*n
        for i in range(n):
            if(visit[i]==False):
                c+=1
                dfs(d,i)
        return c-1
        