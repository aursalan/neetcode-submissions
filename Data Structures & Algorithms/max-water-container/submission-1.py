class Solution:
    def maxArea(self, heights: List[int]) -> int:

        maxValue = 0

        i = 0
        j = len(heights)-1

        while i<j:
            
            currentArea = min(heights[i],heights[j]) * (j-i)
            maxValue = max(currentArea,maxValue)

            if heights[i]<heights[j]:
                i+=1
            
            else:
                j-=1

        return maxValue

            



            

            
        