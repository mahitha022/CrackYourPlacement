class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def countone(i,j):
            cou=0
            for x,y in d:
                nx,ny=i+x,j+y
                
                if(nx<0 or ny<0 or nx>=r or ny>=c ):
                    continue
                if(board[nx][ny] in [1,3]):
                    cou+=1
            return cou
        
        d=[[1,1],[1,0],[1,-1],[0,1],[0,-1],[-1,-1],[-1,0],[-1,1]]
        r=len(board)
        c=len(board[0])
        for i in range(r):
            for j in range(c):
                no1=countone(i,j)
                if(board[i][j]==1):
                    if(no1<2 or no1>3):
                        board[i][j]=3
                   
                else:
                    if(no1==3):
                        board[i][j]=2
                        
        for i in range(r):
            for j in range(c):
                if(board[i][j]==2):
                    board[i][j]=1
                elif(board[i][j]==3):
                    board[i][j]=0