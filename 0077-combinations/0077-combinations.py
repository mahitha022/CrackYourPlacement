class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def back(i,sub,k):
            if(k==0):
                res.append(sub.copy())
                return
            if(i==n):
                return
            
            back(i+1,sub,k)  #not including
            sub.append(i+1)
            back(i+1,sub,k-1)   #including
            sub.pop()

            
        res=[]
        back(0,[],k)
        return res