# https://leetcode.com/problems/container-with-most-water/
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # two pointers, starting on the ends and moving in
        maxArea = 0
        left = 0
        right = len(height) - 1

        while left < right:
            width = right - left
            hh = min(height[left], height[right]) # height is the smallest of the heights of the two pointers
            if height[left] <= height[right]:
                left += 1 # move left pointer right
            else:
                right -= 1 # move right pointer left
            area = hh * width
            if maxArea < area:
                maxArea = area
        return maxArea
