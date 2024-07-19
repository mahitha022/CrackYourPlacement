class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        m=float('-inf')
        last=0
        for i in range(len(points)):
            if(i>=last):
                last=i+1
                
            for j in range(last,len(points)):
                diff=points[j][0]-points[i][0]
                if(diff<=k):
                    diff+=points[i][1]+points[j][1]
                    if(diff>m):
                        m=diff
                        last=j
                else:
                    break
        return m
    
    
        
        