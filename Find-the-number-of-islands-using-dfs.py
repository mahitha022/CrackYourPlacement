def check(nx,ny):
    if(nx>=0 and ny>=0 and nx<r and ny<c and visit[nx][ny]==False and graph[nx][ny]==1):
        return True
    return False


def dfs(i,j):
    visit[i][j]=True
    for x,y in d:
        nx,ny=i+x,j+y
        if(check(nx,ny)):
            dfs(nx,ny)
            


def count():
    res=0
    for i in range(r):
        for j in range(c):
            if(visit[i][j]==False and graph[i][j]==1):
                dfs(i,j)
                res+=1
    return res
                    



graph = [[1, 1, 0, 0, 0],
         [0, 1, 0, 0, 1],
         [1, 0, 0, 1, 1],
         [0, 0, 0, 0, 0],
         [1, 0, 1, 0, 0]]

r=len(graph)
c=len(graph[0])
visit=[False]*r
for i in range(r):
    visit[i]=[False]*c
d=[[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
print(count())
