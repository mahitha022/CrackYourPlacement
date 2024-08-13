class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix=matrix
        self.r=len(self.matrix)
        self.c=len(self.matrix[0])
        
        self.dp=[0]*(self.r+1)
        self.dp=[[0]*(self.c+1) for i in range(self.r+1)]
        
        self.dynamic()
        
    def dynamic(self):

        for i in range(self.r):
            p=0
            for j in range(self.c):
                p+=self.matrix[i][j]
                self.dp[i+1][j+1]=self.dp[i][j+1]+p

                
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.dp[row2+1][col2+1]-self.dp[row1][col2+1]-(self.dp[row2+1][col1]-self.dp[row1][col1])


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)