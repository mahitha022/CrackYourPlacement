# your code goes here
# your code goes here
def check(mid):
	cow=l[0]
	count=1
	for i in range(1,n):
		if(l[i]-cow>=mid):
			cow=l[i]
			count+=1
		if(count==c):
			return True
	return False
	
	
	
def binary(l,c):
	low=l[0]
	high=l[-1]-l[0]
	res=-1
	while(low<=high):
		mid=(low+high)//2
		if(check(mid)):
			res=mid
			low=mid+1
		else:
			high=mid-1
	return res
	
	
	
	
for _ in range(int(input())):
	n,c=map(int,input().split())
	l=[]
	for __ in range(n):
		l.append(int(input()))
	l.sort()
	print(binary(l,c))
