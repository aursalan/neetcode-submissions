class Solution:
    def maxArea(self, heights: List[int]) -> int:

        maxValue = 0

        for i in range(len(heights)):
            for j in range(i+1,len(heights)):

                minHeight = min(heights[i],heights[j])

                minWidth = j-i

                value = minHeight * minWidth 

                maxValue = value if value > maxValue else maxValue
                
        return maxValue

            



            

            
        