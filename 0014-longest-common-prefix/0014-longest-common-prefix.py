class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        a=strs[0]
        res=""
        for i in range(len(a)):
            for s in strs:
                if(i==len(s) or s[i]!=a[i]):
                    return res
            res+=a[i]
        return res