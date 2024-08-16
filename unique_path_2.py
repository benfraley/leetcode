# https://leetcode.com/problems/unique-paths-ii/
# runtime: 91.98%, memory 47.07%
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        # edge cases
        if obstacleGrid[-1][-1] == 1:
            return 0
        if obstacleGrid[0][0] == 1:
            return 0

        # initialize the grid possibilities
        stopAdding = False
        for i in range(len(obstacleGrid[0])):
            if obstacleGrid[0][i] == 1:
                obstacleGrid[0][i] = 'X'
                stopAdding = True
            if not stopAdding:
                obstacleGrid[0][i] += 1

        stopAdding = False
        for i in range(1, len(obstacleGrid)):
            if obstacleGrid[i][0] == 1:
                obstacleGrid[i][0] = 'X'
                stopAdding = True
            if not stopAdding:
                obstacleGrid[i][0] += 1

        # add up the possibilities
        for y in range(1, len(obstacleGrid[0])):
            for x in range(1, len(obstacleGrid)): # 0 position already set
                # none of these should be set, so if they are set set to X
                if obstacleGrid[x][y] == 1:
                    obstacleGrid[x][y] = "X"
                else: 
                    if not isinstance(obstacleGrid[x-1][y], int) and not isinstance(obstacleGrid[x][y-1], int):
                        continue
                    elif not isinstance(obstacleGrid[x-1][y], int):
                        obstacleGrid[x][y] = 0 + obstacleGrid[x][y-1] 
                    elif not isinstance(obstacleGrid[x][y-1], int):
                        obstacleGrid[x][y] = obstacleGrid[x-1][y] + 0 
                    else:
                        obstacleGrid[x][y] = obstacleGrid[x-1][y] + obstacleGrid[x][y-1]
        return obstacleGrid[-1][-1]

