class Solution:
    def minDeletions(self, s: str) -> int:
        c=Counter(list(s))
        l=list(c.values())

        s=set()
        res=0
        for i in range(len(l)):
            while(l[i] in s):
                l[i]-=1
                res+=1
            if(l[i]):
                s.add(l[i])
                
        return res