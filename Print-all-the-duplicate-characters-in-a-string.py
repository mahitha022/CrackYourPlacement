def printDups(s):
    d={}
    for i in s:
        d[i]=d.get(i,0)+1
    for i in d:
        if(d[i]>1):
            print(i,"count: ",d[i])

s=input()
printDups(s)
