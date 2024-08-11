#User function Template for python3

class Solution:
    def longestCommonSubstr(self, s1, s2):
        # code here
        dp=[0]*len(s1)
        dp=[[0]*len(s2) for i in range(len(s1))]
        m=0
        for i in range(len(s1)):
            for j in range(len(s2)):
                if(s1[i]==s2[j]):
                    if(i==0 or j==0):
                        dp[i][j]=1
                    else:
                        dp[i][j]=dp[i-1][j-1]+1
                    m=max(dp[i][j],m)

        return m

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S1 = input().strip()
        S2 = input().strip()
        ob = Solution()
        print(ob.longestCommonSubstr(S1, S2))

# } Driver Code Ends