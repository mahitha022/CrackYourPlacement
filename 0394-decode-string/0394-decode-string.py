class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        
        for i in s:
            
            if(i==']'):
                word=""
                while(stack and stack[-1]!='['):
                    word=stack.pop()+word
                
                stack.pop()
                num=""
                while(stack and stack[-1].isdigit()):
                    num=stack.pop()+num
                
                word=word*(int(num))
                stack.append(word)
                
                
            else:
                stack.append(i)
                
        return "".join(stack)