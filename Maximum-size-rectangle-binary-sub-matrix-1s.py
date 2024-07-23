def change(mat):
    for i in range(1,r):
        for j in range(c):
            if(mat[i][j]==1):
                mat[i][j]+=mat[i-1][j]

def marea(row):
    s=[[0,row[0]]]
    m=0
    for i in range(1,c):
        
        if(row[i]<s[-1][1]):
            while(s and row[i]<s[-1][1]):
                ind,val=s.pop()
                m=max(m,(i-ind)*val)
            s.append([ind,row[i]])
        else:
            s.append([i,row[i]])
    
    for ind,val in s:
        m=max(m,(c-ind)*val)
    return m
    
    
    
mat=[[0, 1, 1, 0],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 0, 0]]
r=len(mat)
c=len(mat[0])
change(mat)
res=0
for row in mat:
    res=max(res,marea(row))
            
print(res)
    
