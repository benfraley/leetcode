# O(n**2) but I came up with it myself
# this was a hard problem so I'm giving myself some credit here
# https://neetcode.io/problems/largest-rectangle-in-histogram
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0 
        for ch in range(1, max(heights)+1):
            area = 0
            mArea = 0
            for h in heights:
                if h >= ch:
                    area += ch
                    mArea = max(mArea, area)
                    print(ch, h, area)
                else:
                    area = 0
            maxArea = (max(maxArea, mArea))
        return maxArea
        