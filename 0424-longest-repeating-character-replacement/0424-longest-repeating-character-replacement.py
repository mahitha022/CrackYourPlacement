class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d={s[0]:1}
        i=0
        j=0
        res=0
        
        while(j<len(s)):
            
            if((j-i+1)-max(d.values())<=k):
                res=max(res,j-i+1)
                j+=1
                if(j<len(s)):
                    d[s[j]]=d.get(s[j],0)+1
            
            else:
                d[s[i]]-=1
                i+=1
        
        return res