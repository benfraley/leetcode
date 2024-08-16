# https://leetcode.com/problems/valid-number/
# runtime 60.15%, memory 15.67%
class Solution:
    def isNumber(self, s: str) -> bool:
        if "inf" in s.lower(): return False
        if "nan" in s.lower(): return False
        import re
        r = re.split(r'\s+|[eE]', s)
        if len(r) == 1: # didnt split
            try:
                float(s)  
                return True
            except ValueError:
                return False
        elif len(r) > 2:
            return False
        else:
            try:
                int(r[1])
                float(r[0])
                return True
            except ValueError:
                return False

        