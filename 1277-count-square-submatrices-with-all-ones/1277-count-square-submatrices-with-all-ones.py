class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if(matrix[i][j]>0):
                    matrix[i][j]=min(matrix[i][j-1], matrix[i-1][j-1], matrix[i-1][j])+1
                
        
        s=0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                s+=matrix[i][j]
                
        #print(matrix)
        return s