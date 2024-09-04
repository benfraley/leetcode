# https://neetcode.io/problems/trapping-rain-water
# this was a tough one! My solution was to work from the top of the "landscape" 
# and work my way down, finding the area inbetween the two points, then 
# reducing those points by 1 so that their caught by the next iteration
class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0
        maxHeight = max(height) # the highest peak
        for i in range(maxHeight, 0, -1): # work our way down
            level_index = [] # how many peaks we find
            for j in range(len(height)): 
                if height[j] == i:
                    level_index.append(j) # get how many peak we have at the current level
                    height[j] -= 1 # reduce that peak by one so that it's found by the next iteration
            # print(i, level_index)
            # print("heights", height)
            for k in range(len(level_index)):
                if k+1 < len(level_index): # has to be more than one to catch water
                    area_to_add = level_index[k+1] - level_index[k] - 1
                    # print("adding", area_to_add)
                    area += level_index[k+1] - level_index[k] - 1
        return area
                    