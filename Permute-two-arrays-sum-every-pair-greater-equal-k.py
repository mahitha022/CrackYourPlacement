def check(a,b):
    for i in range(n):
        if(a[i]+b[i]!=k):
            return False
    return True
    

a = [2, 1, 3]
b = [5, 8, 9]
k = 10
n=len(a)
a.sort()
b.sort(reverse=True)
print(check(a,b))
