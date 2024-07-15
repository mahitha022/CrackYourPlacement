class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        j=1
        mprofit=0
        while(j<len(prices)):
            cprofit=prices[j]-prices[i]
            if(prices[i]<prices[j]):
                mprofit=max(mprofit,cprofit)
            else:
                i=j
            j+=1
        return mprofit