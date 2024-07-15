class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        marea=0
        while(i<j):
            area=(j-i)*min(height[i],height[j])
            marea=max(area,marea)
            if(height[i]<height[j]):
                i+=1
            else:
                j-=1
        return marea