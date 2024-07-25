class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        res=[]
        l=[]
        length=0
        i=0
        while(i<len(words)):
            
            if(length+len(l)+len(words[i])>maxWidth):
                
                remlength = maxWidth - length
                space = remlength // max(1,len(l)-1)
                remspace = remlength % max(1,len(l)-1)
                
                for j in range(max(1,len(l)-1)):
                    l[j]+=" "*space
                    if(remspace):
                        l[j]+=" "
                        remspace-=1
                res.append("".join(l))
                l=[]
                length=0
            
            
            l.append(words[i])
            length+=len(words[i])
            i+=1
            
        last=" ".join(l)
        res.append(last+" "*(maxWidth-len(last)))
        return res