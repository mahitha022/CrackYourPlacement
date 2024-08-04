#User function Template for python3

class Solution:
    
    #Function to find maximum of minimums of every window size.
    def maxOfMin(self,arr,n):
        # code here
        def left(ind):
            for j in range(ind-1,-1,-1):
                if(arr[ind]>arr[j]):
                    return ind-(j+1)
            return ind
            
        def right(ind):
            for j in range(ind+1,n):
                if(arr[ind]>arr[j]):
                    return (j-1)-ind
            return n-ind-1
        
        res=[0]*(n+1)
        for i in range(n):
            m=left(i)+right(i)+1
            res[m]=max(arr[i],res[m])
        
        for i in range(n-1,0,-1):
            res[i]=max(res[i],res[i+1])

        return res[1:]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        ob=Solution()
        res = ob.maxOfMin(a,n)
        for i in range (len (res)):
            print (res[i], end = " ")
        print ()

# } Driver Code Ends