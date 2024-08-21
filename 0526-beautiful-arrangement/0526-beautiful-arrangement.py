class Solution:
    def countArrangement(self, n: int) -> int:
        
        def back(i):
            if(i==len(l)):
                self.c+=1
                return
            
            for ind in range(i,n+1):
                if(i%l[ind]==0 or l[ind]%i==0):
                    l[ind],l[i]=l[i],l[ind]
                    back(i+1)
                    l[i],l[ind]=l[ind],l[i]
        
        self.c=0
        l=[i for i in range(n+1)]
        back(1)
        return self.c