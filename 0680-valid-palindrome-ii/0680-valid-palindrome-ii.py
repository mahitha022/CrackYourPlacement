class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(p):
            if(p==p[::-1]):
                return True
            return False
        
        i=0
        j=len(s)-1
        if(check(s)):
            return True
        while(i<j):
            if(s[i]!=s[j]):
                if(check(s[:i]+s[i+1:])):
                    return True
                elif(check(s[:j]+s[j+1:])):
                    return True
                else:
                    return False
            i+=1
            j-=1
        