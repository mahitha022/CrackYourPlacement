class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        l1=[]
        l2=[]
        for i in s:
            if(l1 and i=='#' ):
                l1.pop()
            if(i!='#'):
                l1.append(i)
    
        for i in t:
            if(l2 and i=='#' ):
                l2.pop()
            if(i!='#'):
                l2.append(i)
        
        return l1==l2