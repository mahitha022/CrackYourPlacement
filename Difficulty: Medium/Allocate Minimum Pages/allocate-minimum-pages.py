class Solution:
    
    #Function to find minimum number of pages.
    def findPages(self,n ,arr ,m):
        #code here
        def check(mid):
            student=1
            page=0
            
            for i in range(n):
                if(arr[i]>mid):
                    return False
                if(arr[i]+page>mid):
                    student+=1
                    page=arr[i]
                else:
                    page+=arr[i]
                    
            if(student<=m):
                return True
            return False
            
        
        if(m>n):
            return -1
        low=arr[0]
        high=sum(arr)
        res=float('inf')
        
        while(low<=high):
            mid=(low+high)//2
            
            if(check(mid)):
                res=mid
                high=mid-1
            else:
                low=mid+1
        
        return res
                
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        n = int(input())

        arr = [int(x) for x in input().strip().split()]
        m = int(input())

        ob = Solution()

        print(ob.findPages(n, arr, m))

# } Driver Code Ends