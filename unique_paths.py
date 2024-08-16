# https://leetcode.com/problems/unique-paths/
# had to look up the math lol
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # has to be m-1 moves down and n-1 moves right
        # total moves is (m-1) + (n-1), thus m+n-2
        # combination formaula N! / (r!(N-r)!) - N is number of moves and r is our choice of movement
        # so, if moving down (m-1), formula is:
        # (m+n-2)! / ((m-1)!(m+n-2 - m -1)!)
        # (m+n-2)! / ((m-1)!(n-1)!) - note: would get the same result if moving right (r=n-1)
        import math

        return int(math.factorial(m+n-2) / math.factorial(m-1) / math.factorial(n-1))
