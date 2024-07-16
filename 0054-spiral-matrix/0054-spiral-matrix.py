class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l=[]
        r=len(matrix)
        c=len(matrix[0])
        start=0
        end=1
        total=r*c
        while(len(l)<total):
            for i in range(start,c):
                l.append(matrix[start][i])
            if(len(l)==total):
                break
            for i in range(end,r):
                l.append(matrix[i][c-1])
            if(len(l)==total):
                break
            for i in range(c-2,start-1,-1):
                l.append(matrix[r-1][i])
            if(len(l)==total):
                break
            for i in range(r-2,start,-1):
                l.append(matrix[i][start])
            start+=1
            end+=1
            r-=1
            c-=1
        return l