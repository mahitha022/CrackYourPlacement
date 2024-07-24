def cost(arr):
    if(n%2==0):
        m=(arr[n//2]+arr[(n//2)-1])//2
    else:
        m=arr[n//2]
    
    c=0
    for i in range(n):
        c+=abs(m-arr[i])
    return c


arr=[4,6,8,10]
n=len(arr)
arr.sort()
print(cost(arr))
