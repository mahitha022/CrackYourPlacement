class Solution:
    def reverseWords(self, s: str) -> str:
        l=[]
        r=""
        for i in s:
            if(i.isalnum()):
                r+=i
            elif(r.isalnum()):
                l.append(r)
                r=""
        if(r.isalnum()):
            l.append(r)
        return ' '.join(l[::-1])
        