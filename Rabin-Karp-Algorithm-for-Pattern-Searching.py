def rabin(txt,pat):
    tlen=len(txt)
    plen=len(pat)
    thash=0
    phash=0
    h=1
    for i in range(plen-1):
        h=(h*base)%prime
    for i in range(plen):
        thash=(thash*base+ord(txt[i]))%prime
        phash=(phash*base+ord(pat[i]))%prime
    for i in range(tlen-plen+1):
        if(thash==phash):
            c=0
            for j in range(plen):
                if(pat[j]==txt[i+j]):
                    c+=1
                else:
                    break
            if(c==plen):
                print(i)
        if(i<tlen-plen):
            thash=(base*(thash-ord(txt[i])*h)+ord(txt[i+plen]))%prime
            if(thash<0):
                thash+=prime
                
                
    
    
txt="ABCDEBCDF"
pat="BCD"
prime=101
base=256
rabin(txt,pat)
