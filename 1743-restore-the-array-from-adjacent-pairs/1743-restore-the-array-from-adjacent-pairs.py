class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        d={}
        visit=[]
        
        for i,j in adjacentPairs:
            d.setdefault(i,[]).append(j)
            d.setdefault(j,[]).append(i)
            
        for k,v in d.items():
            if(len(v)==1):
                visit=[k,v[0]]
                break
        
        while(len(visit)<len(d)):
            
            last=visit[-1]
            second_last=visit[-2]
            next_ele=d[last]
            
            if(next_ele[0]==second_last):
                visit.append(next_ele[1])
            else:
                visit.append(next_ele[0])
        
        return visit