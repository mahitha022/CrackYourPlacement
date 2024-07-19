class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        l=[[0,heights[0]]]
        m=0
        n=len(heights)
        for i in range(1,n):
            
            if(heights[i]<l[-1][1]):
                while(l and heights[i]<l[-1][1]):
                    ind=l.pop()
                    m=max(m,(i-ind[0])*ind[1])
                l.append([ind[0],heights[i]])
                
            else:
                l.append([i,heights[i]])
                
        for i,j in l:
            m=max(m,(n-i)*j)
            
        return m