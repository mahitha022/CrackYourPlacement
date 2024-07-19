class Solution:
    def simplifyPath(self, path: str) -> str:
        path+='/'
        l=[]
        s=""
        for i in path:
            if(i=='/'):
                if(s=='..'):
                    if(l):
                        l.pop()
                elif(len(s)>0 and s!='.'):
                    l.append(s)
                s=""
                
            else:
                s+=i
        return '/'+'/'.join(l)
        