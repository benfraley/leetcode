# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/submissions/1417106998/?envType=daily-question&envId=2024-10-09
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        o, c = 0, 0
        for ch in s:
            if ch == "(":
                o += 1
            else:
                if o > 0:
                    o -= 1
                else:
                    c += 1
        return o+c
