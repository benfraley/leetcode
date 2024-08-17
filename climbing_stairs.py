# https://leetcode.com/problems/climbing-stairs/
# runtime 83.97%, memory 14.33%
class Solution:
    def climbStairs(self, n: int) -> int:
        # this is like the unique paths, in that we're calculating the ways to get to a step
        if n == 0 or n == 1: # edge cases
            return 1

        steps = [0] * (n + 1) # init all the steps besides 0 and 1 to 0
        steps[0] = steps[1] = 1 # these only have one way to get to them

        for i in range(2, n+1): # 2nd step to the last
            steps[i] = steps[i-1] + steps[i-2] # you can get there from 1 or 2 steps before, so add up their values
        return steps[n] # return the last index