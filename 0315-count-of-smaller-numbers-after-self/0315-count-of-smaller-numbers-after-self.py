class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def mergeSort(temp,l,r,res):
            if(l>=r):
                return
            m=(l+r)//2
            mergeSort(temp,l,m,res)
            mergeSort(temp,m+1,r,res)
            merge(temp,l,m,r,res)
            
            
        def merge(temp,l,m,r,res):
            i=l
            j=m+1
            inv=0
            
            while(i<=m and j<=r):
                if(temp[i][1]<=temp[j][1]):
                    res[temp[i][0]]+=inv
                    i+=1
                else:
                    inv+=1
                    j+=1
            
            
            while(i<=m):
                res[temp[i][0]]+=(r-m)
                i+=1
            
                
            temp[l:r+1]=sorted(temp[l:r+1], key=lambda x:x[1])
            
        
        n=len(nums)
        res=[0]*n
        temp=list(enumerate(nums))
        mergeSort(temp,0,n-1,res)
        return res
        
        