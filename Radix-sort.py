import math




arr = [170, 45, 75, 90, 802, 24, 2, 66]
m=max(arr)
digit=int(math.log(m,10))+1
power=0
n=len(arr)

for i in range(digit):
    count=[0]*10
    div=10**power
    
    for j in range(n):
        rem=(arr[j]//div)%10
        count[rem]+=1
    
    for j in range(1,10):
        count[j]=count[j]+count[j-1]
    
    t=[0]*n
    
    for j in range(n-1,-1,-1):
        rem=(arr[j]//div)%10
        count[rem]-=1
        t[count[rem]]=arr[j]
    
    for j in range(n):
        arr[j]=t[j]
    
    power+=1
print(t)
