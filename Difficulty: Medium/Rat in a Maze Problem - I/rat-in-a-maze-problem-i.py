from typing import List

class Solution:
    def findPath(self, m: List[List[int]]) -> List[str]:
        # code here
        
        
        def dfs(i,j,s):
            if(i==n-1 and j==n-1):
                res.append(s)
                return
            if(i>=n or j>=n or i<0 or j<0 or m[i][j]==0):
                return
            
            m[i][j]=0
            dfs(i-1,j,s+'U')
            dfs(i+1,j,s+'D')
            dfs(i,j-1,s+'L')
            dfs(i,j+1,s+'R')
            
            
            m[i][j]=1

            
        res=[]
        n=len(m)
        if(m[0][0]==0 or m[n-1][n-1]==0):
            return ['-1']
        dfs(0,0,"")
        if(len(res)==0):
            return ['-1']
        return res
        

#{ 
 # Driver Code Starts
# Main function to read input and output the results
if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        m = []
        for i in range(n):
            m.append(list(map(int, input().strip().split())))
        obj = Solution()
        result = obj.findPath(m)
        result.sort()
        if len(result) == 0:
            print(-1)
        else:
            print(" ".join(result))

# } Driver Code Ends