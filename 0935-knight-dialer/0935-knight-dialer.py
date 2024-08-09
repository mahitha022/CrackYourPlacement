class Solution:
    def knightDialer(self, n: int) -> int:
        if(n==1):
            return 10
        
        dp=[1]*10
        jump=[[4,6],[6,8],[7,9],[4,8],[0,3,9],[],[0,1,7],[2,6],[1,3],[2,4]]
        
        mod=10**9+7
        
        for _ in range(n-1):
            temp_dp=[0]*10
            for i in range(10):
                for j in jump[i]:
                    temp_dp[j]=(temp_dp[j]+dp[i])%mod
            dp=temp_dp
        
        s=0
        for i in dp:
            s=(s+i)%mod
        return s