class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        l=[]
        for i in s:
            if(l and l[-1][0]==i):
                l[-1][1]+=1
            
            else:
                l.append([i,1])
            if(l[-1][1]==k):
                l.pop()
        res=""
        for alp,no in l:
            res+=(alp*no)
        
        return res