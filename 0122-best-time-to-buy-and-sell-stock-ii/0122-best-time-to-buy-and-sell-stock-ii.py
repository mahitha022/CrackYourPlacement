class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=prices[0]
        mprofit=0
        for i in range(1,len(prices)):
            if(buy<prices[i]):
                mprofit+=prices[i]-buy
            buy=prices[i]
        return mprofit

        