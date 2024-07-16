class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        for i in s:
            if(i in ['(','{','[']):
                l.append(i)
            else:
                if(len(l)==0):
                    return False
                check=l.pop()
                if(check=='('):
                    if(i!=')'):
                        return False
                elif(check=='{'):
                    if(i!='}'):
                        return False
                elif(check=='['):
                    if(i!=']'):
                        return False
        if(len(l)==0):
            return True
        return False