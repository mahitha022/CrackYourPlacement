class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        i,j,c,winsum=0,0,0,0
        n=len(cardPoints)
        s=sum(cardPoints)
        window=n-k
        if(window==0):
            return s
        while(j<n):
            winsum+=cardPoints[j]
            if(j-i+1==window):
                c=max(c,s-winsum)
                winsum-=cardPoints[i]
                i+=1
            j+=1
            
            
        return c
                
        