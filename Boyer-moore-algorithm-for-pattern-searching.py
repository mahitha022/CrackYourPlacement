def badMatch(txt,pat):
    bad={}
    
    for i in range(patlen):
        bad[pat[i]]=max(1,patlen-1-i)

    return bad

def boyer(txt,pat):
    bad=badMatch(txt,pat)
    i=0
    
    while(i<=txtlen-patlen):
        j=patlen-1
        
        while(j>=0 and txt[i+j]==pat[j]):
            j-=1
            
        if(j<0):
            print("found: ",i)
            
            if(i+patlen<txtlen):
                if(txt[i+patlen] in bad):
                    i+=patlen-bad[txt[i+patlen]]
                    
                else:
                    i+=patlen+1
            else:
                i+=1
                
        else:
            if(txt[i+j] in bad):
                i+=max(1,j-bad[txt[i+j]])
                
            else:
                i+=max(1,j+1)
                
            

txt = "AABAACAADAABAABA"
pat = "AABA"
patlen=len(pat)
txtlen=len(txt)
boyer(txt,pat)
