# User function Template for Python3

class Solution:
    def equalPartition(self, N, arr):
        # code here
        total=sum(arr)
        if(total%2==1):
            return False
        t=total//2
        s=set()
        s.add(0)
        for i in range(N-1,-1,-1):
            tmp=set()
            for j in s:
                tmp.add(j+arr[i])
                tmp.add(j)
            s=tmp
        
        if(t in s):
            return True
        return False


#{ 
 # Driver Code Starts
# Initial Template for Python3

import sys
input = sys.stdin.readline
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for it in range(N):
            arr[it] = int(arr[it])
        
        ob = Solution()
        if (ob.equalPartition(N, arr) == 1):
            print("YES")
        else:
            print("NO")
# } Driver Code Ends