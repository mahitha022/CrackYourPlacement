class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r=len(matrix)
        c=len(matrix[0])
        firstrow=False
        firstcolumn=False
        for i in range(r):
            for j in range(c):
                if(i==0 or j==0):
                    if(matrix[0][j]==0):
                        firstrow=True
                    if(matrix[i][0]==0):
                        firstcolumn=True
                elif(matrix[i][j]==0):
                    matrix[0][j]=0
                    matrix[i][0]=0
                
        for i in range(1,r):
            for j in range(1,c):
                if(matrix[0][j]==0 or matrix[i][0]==0):
                    matrix[i][j]=0
        if(firstrow):
            for j in range(c):
                matrix[0][j]=0
        if(firstcolumn):
            for i in range(r):
                matrix[i][0]=0