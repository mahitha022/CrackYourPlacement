class Solution:
    def isNumber(self, s: str) -> bool:
        digit, point, e, sign =False, False, False, False
        
        for i in s:
            
            if(i in '0123456789'):
                digit=True
                
            elif(i=='.'):
                if(point or e):
                    return False
                point=True
                
            elif(i in 'eE'):
                if(e or digit==False):
                    return False
                e=True
                sign=False
                digit=False
                point=False
                
            elif(i in '+-'):
                if(sign or digit or point):
                    return False
                sign=True
                
            else:
                return False
        
        return digit