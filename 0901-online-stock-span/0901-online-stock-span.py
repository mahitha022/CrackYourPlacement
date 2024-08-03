class StockSpanner:

    def __init__(self):
        self.l=[]
        

    def next(self, price: int) -> int:
        cost=1
        while(self.l and price>=self.l[-1][0]):
            val=self.l.pop()
            cost+=val[1]
            
        self.l.append([price,cost])
        return cost

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)