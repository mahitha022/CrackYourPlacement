class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans=[0]*len(temperatures)
        l=[]
        
        for i in range(len(temperatures)):
            curr=temperatures[i]
            while(l and l[-1][0]<curr):
                ans[l[-1][1]]=i-l[-1][1]
                l.pop()
            l.append([curr,i])
        return ans