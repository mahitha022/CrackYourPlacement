class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def check(palin):
            i=0
            j=len(palin)-1
            while(i<=j):
                if(palin[i]!=palin[j]):
                    return False
                i+=1
                j-=1
            
            return True
        
        def back(i):
            if(i==n):
                res.append(tmplist.copy())
                return
            
            for ind in range(i,n):
                tmp=s[i:ind+1]
                if(check(tmp)):
                    tmplist.append(tmp)
                    back(ind+1)
                    tmplist.pop()
        
        tmplist=[]
        res=[]
        n=len(s)
        back(0)
        return res