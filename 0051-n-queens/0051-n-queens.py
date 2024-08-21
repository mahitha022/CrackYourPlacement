class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def back(r):
            if(r==n):
                copy=["".join(row) for row in chess]
                res.append(copy)
                return
            
            for c in range(n):
                if(c in col or (r-c) in negdia or (r+c) in posdia):
                    continue
                
                col.add(c)
                negdia.add(r-c)
                posdia.add(r+c)
                chess[r][c]="Q"
                
                back(r+1)
                
                col.remove(c)
                negdia.remove(r-c)
                posdia.remove(r+c)
                chess[r][c]="."
                
                
                
                
        chess=[["."]*n for i in range(n)]
        res=[]
        col=set()
        negdia=set() #(r-c)
        posdia=set() #(r+c)
        back(0)
        return res