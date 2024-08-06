class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def back(i,sub,k):
            if(k==0):
                res.append(sub.copy())
                return
            if(i==n):
                return
            
            back(i+1,sub,k)  #not including
            
            back(i+1,sub+[i+1],k-1)   #including

            
        res=[]
        back(0,[],k)
        return res