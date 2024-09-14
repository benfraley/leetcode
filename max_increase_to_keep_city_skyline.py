# https://leetcode.com/problems/max-increase-to-keep-city-skyline/
# https://leetcode.com/problems/max-increase-to-keep-city-skyline/solutions/5786824/readable-and-understandable-python-solution/
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        # get max of the row and column, then take the minimum
        maxRows = [max(row) for row in grid]
        maxCols = list(map(max, zip(*grid))) # the * operator transposes the grid
        added = 0
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                # we can't increase the size of the position if it's >= the minimum of the max row or max column
                newVal = min(maxRows[y], maxCols[x])
                if grid[y][x] < newVal:
                    added += (newVal - grid[y][x]) # append how much we added
                    #grid[y][x] = newVal # update the grid just to make sure it worked
        #print(grid)
        return added


                