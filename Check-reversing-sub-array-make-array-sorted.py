def check(arr):
    x,y=-1,-1
    for i in range(n-1):
        if(arr[i]>arr[i+1]):
            if(x==-1):
                x=i
            y=i+1
    if(x==-1):
        return True
    
    i=x
    j=y
    while(i<j):
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1

    for i in range(n-1):
        if(arr[i]>arr[i+1]):
            return False
    return True
    

arr=[1,2,5,4,3]
n=len(arr)
print(check(arr))
