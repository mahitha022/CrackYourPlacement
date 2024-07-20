class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        w={}
        c={}
        for i in t:
            c[i]=c.get(i,0)+1
        have=0
        need=len(c)
        res=float('inf')
        resl=[-1,-1]
        
        l=0
        for r in range(len(s)):
            w[s[r]]=w.get(s[r],0)+1
            if(s[r] in c and w[s[r]]==c[s[r]]):
                have+=1
            while(have==need):
                if(r-l+1<res):
                    res=r-l+1
                    resl=[l,r]
                w[s[l]]-=1
                if(s[l] in c and w[s[l]]<c[s[l]]):
                    have-=1
                l+=1
        return s[resl[0]:resl[1]+1]
        