#User function Template for python3

class Solution:
    def allPalindromicPerms(self, S):
        # code here 
        
        def check(palin,i,j):
            
            while(i<j):
                if(palin[i]!=palin[j]):
                    return False
                i+=1
                j-=1
            return True
        
        def back(i):
            if(i==len(S)):
                res.append(tmplist.copy())
                return
            
            
            for ind in range(i,len(S)):
                
                if(check(S,i,ind)):
                    tmplist.append(S[i:ind+1])
                    back(ind+1)
                    tmplist.pop()
        res=[]
        tmplist=[]
        back(0)
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S=input()
        
        ob = Solution()
        allPart = ob.allPalindromicPerms(S)
        for i in range(len(allPart)): 
            for j in range(len(allPart[i])): 
                print(allPart[i][j], end = " ") 
            print() 
# } Driver Code Ends