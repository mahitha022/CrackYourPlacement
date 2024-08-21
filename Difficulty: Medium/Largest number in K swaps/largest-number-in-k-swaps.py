#User function Template for python3

class Solution:
    
    #Function to find the largest number after k swaps.
    def findMaximumNum(self,s,k):
        #code here
        
        def fun(s,k,i):
            if(s>tmp[0]):
                tmp[0]=s
            if(k==0 or i==len(s)):
                return
            
            m=max(s[i:])
            if(s[i]!=m):
                for j in range(i+1,len(s)):
                    if(s[j]==m):
                        swap=s[:i]+s[j]+s[i+1:j]+s[i]+s[j+1:]
                        
                    
                        fun(swap,k-1,i+1)
                            #s=s[:i]+s[j]+s[i+1:j]+s[i]+s[j+1:]
                
            fun(s,k,i+1)
            
        tmp=["0"]    
        fun(s,k,0)
        return tmp[0]



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        k = int(input())
        s = input()
        ob=Solution()
        print(ob.findMaximumNum(s,k))

# } Driver Code Ends