

class Solution:
    
    #Function to find the minimum number of swaps required to sort the array.
	def minSwaps(self, nums):
		#Code here
		temp=[]
		n=len(nums)
		for i in range(n):
		    temp.append([nums[i],i])
		temp.sort()
		c=0
		i=0
		while(i<n):
		    ind=temp[i][1]
		    if(i!=ind):
		        c+=1
		        temp[i],temp[ind]=temp[ind],temp[i]
		        i-=1
		    i+=1

		        
		return c
		        

#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		obj = Solution()
		ans = obj.minSwaps(nums)
		print(ans)

# } Driver Code Ends