# https://leetcode.com/problems/minimum-window-substring/
# only passing 264/268 test cases, will revisit
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if s == t:
            return s
        
        tcount = Counter(t)
        #print("looking for: ", tcount)
        window = ""
        l, r = 0,len(t)
        ret = {}
        while l < len(s) - r + 1:
            lword = s[l:l+r]
            lcount = Counter(lword)
            if all(tcount[key] <= lcount[key] for key in tcount):
                ret[len(lword)] = (l, l+r)
                l += 1
                r = len(t)
            else:
                if l + r > len(s):
                    l += 1
                else:
                    r += 1
        if len(ret) == 0:
            return ""
        else:
            start, end = ret[min(ret.keys())]
            return s[start:end]