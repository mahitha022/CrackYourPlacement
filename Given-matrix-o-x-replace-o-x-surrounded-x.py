
def changeToHyphen(mat):
    for i in range(r):
        for j in range(c):
            if(mat[i][j]=='O'):
                mat[i][j]='-'
    changeCorners(mat)
    

def changeCorners(mat):
    def check(nx,ny):
        if(nx>=0 and ny>=0 and nx<r and ny<c and mat[nx][ny]=='-'):
            return True
        return False
        
    def dfs(i,j):
        mat[i][j]='O'
        for x,y in d:
            nx,ny=i+x,j+y
            if(check(nx,ny)):
                dfs(nx,ny)
    
    #first row
    for j in range(c):
        if(mat[0][j]=='-'):
            dfs(0,j)
    #first column
    for i in range(r):
        if(mat[i][0]=='-'):
            dfs(i,0)
    #last column
    for i in range(r):
        if(mat[i][c-1]=='-'):
            dfs(i,c-1)
    #last row
    for j in range(c):
        if(mat[r-1][j]=='-'):
            dfs(r-1,j)
    
    changeRest(mat)
    

def changeRest(mat):
    for i in range(1,r-1):
        for j in range(1,c-1):
            if(mat[i][j]=='-'):
                mat[i][j]='X'
                


mat = [ [ 'X', 'O', 'X', 'O', 'X', 'X' ], 
        [ 'X', 'O', 'X', 'X', 'O', 'X' ], 
        [ 'X', 'X', 'X', 'O', 'X', 'X' ], 
        [ 'O', 'X', 'X', 'X', 'X', 'X' ], 
        [ 'X', 'X', 'X', 'O', 'X', 'O' ], 
        [ 'O', 'O', 'X', 'O', 'O', 'O' ] ]

r=len(mat)
c=len(mat[0])
d=[[-1,0],[1,0],[0,-1],[0,1]]
changeToHyphen(mat)
for i in mat:
    print(i)
