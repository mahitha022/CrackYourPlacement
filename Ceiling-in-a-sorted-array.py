def binaryceil(l,r):
    if(x<=arr[l]):
        return l
    if(x>arr[r]):
        return -1
    m=(l+r)//2
    if(x==arr[m]):
        return m
    elif(x<arr[m]):
        if(m-1>=l and arr[m-1]<x):
            return m
        return binaryceil(l,m-1)
    else:
        if(m+1<=r and arr[m+1]>=x):
            return m+1
        return binaryceil(m+1,r)


arr = [1, 2, 8, 10, 10, 12, 19]
n = len(arr)
x = 20
print(binaryceil(0,n-1))
