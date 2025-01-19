class Solution:
    def trap(self, heights: List[int]) -> int:

        maxes = [0 for x in range(len(heights))]

        leftMax = 0

        for i in range(len(heights)):
            height = heights[i]
            maxes[i] = leftMax
            leftMax = max(height, leftMax)

        rightMax = 0

        for i in reversed(range(len(heights))):
            height = heights[i]
            minHeight = min(rightMax, maxes[i])
            if height < minHeight:
                maxes[i] = minHeight - height
            else:
                maxes[i] = 0
            rightMax = max(rightMax, height)

        return sum(maxes)

        