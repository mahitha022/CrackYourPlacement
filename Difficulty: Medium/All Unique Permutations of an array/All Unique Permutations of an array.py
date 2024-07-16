#User function Template for python3

class Solution:
    def uniquePerms(self, arr, n):
        # code here 
        l=[]
        res=[]
        d={}
        for i in arr:
            d[i]=d.get(i,0)+1
        
        
        def dfs():
            if(len(l)==len(arr)):
                res.append(l.copy())
                return
            
            for i in d:
                if(d[i]>0):
                    
                    l.append(i)
                    d[i]-=1
                    
                    dfs()
                    
                    d[i]+=1
                    l.pop()
                    
        dfs()
        res.sort()
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n=int(input())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        res = ob.uniquePerms(arr,n)
        for i in range(len(res)):
            for j in range(n):
                print(res[i][j],end=" ")
            print()
# } Driver Code Ends
