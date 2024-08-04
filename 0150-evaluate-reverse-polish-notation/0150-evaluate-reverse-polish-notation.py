class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        l=[]
        for i in tokens:
            if(i in ['+','-','*','/']):
                b=l.pop()
                a=l.pop()
                if(i=='+'):
                    l.append(a+b)
                elif(i=='-'):
                    l.append(a-b)
                elif(i=='*'):
                    l.append(a*b)
                else:
                    if(a<0 and b<0):
                        l.append((a//b))
                    elif(a<0 ):
                        l.append(-(-a//b))
                    elif(b<0):
                        l.append(-(a//-b))
                    else:
                        l.append(a//b)
            else:
                l.append(int(i))
            #print(l)
        return l[0]