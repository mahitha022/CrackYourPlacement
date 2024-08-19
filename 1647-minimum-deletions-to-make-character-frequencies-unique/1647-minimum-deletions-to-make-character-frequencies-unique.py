class Solution:
    def minDeletions(self, s: str) -> int:
        d={}
        for i in s:
            d[i]=d.get(i,0)+1

        s=set()
        res=0
        for i in d.values():
            while(i in s):
                i-=1
                res+=1
            if(i):
                s.add(i)
                
        return res