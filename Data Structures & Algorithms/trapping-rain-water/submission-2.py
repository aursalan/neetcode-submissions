class Solution:
    def trap(self, height):
        
        i, j = 0, len(height)

        total = 0

        left = [0] * len(height)
        right = [0] * len(height) 

        maxValue = 0

        for i in range(len(height)):
            left[i] = maxValue
            if height[i]>maxValue:
                maxValue=height[i]

        maxValue = 0

        for i in range(len(height)-1,-1,-1):
            right[i] = maxValue
            if height[i]>maxValue:
                maxValue=height[i]

        for i in range(len(height)):
            
            total+= max(0,min(left[i],right[i]) - height[i])

        return total