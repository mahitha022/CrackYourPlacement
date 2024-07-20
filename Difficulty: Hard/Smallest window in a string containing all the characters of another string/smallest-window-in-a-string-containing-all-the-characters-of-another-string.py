#User function Template for python3


class Solution:
    
    #Function to find the smallest window in the string s consisting
    #of all the characters of string p.
    def smallestWindow(self, s, p):
        #code here
        
        w={}
        c={}
        res=float('inf')
        resl=[-1,-1]
        for i in p:
            c[i]=c.get(i,0)+1
        have=0
        need=len(c)
        l=0
        for r in range(len(s)):
            w[s[r]]=w.get(s[r],0)+1
            if(s[r] in c and w[s[r]]==c[s[r]]):
                have+=1
            while(have==need):
                if(r-l+1<res):
                    resl=[l,r]
                    res=r-l+1
                w[s[l]]-=1
                if(s[l] in c and w[s[l]]<c[s[l]]):
                    have-=1
                l+=1
        if(resl[0]==-1):
            return "-1"
        return s[resl[0]:resl[1]+1]
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        p=str(input())
        ob = Solution()
        print(ob.smallestWindow(s,p))
# } Driver Code Ends