class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        cur, max = "", ""
        for i in range(len(s)):
            for char in (s[i:]):
                if char not in cur:
                    cur += char
                else:
                    if len(cur) > len(max):
                        max = cur
                    cur = ""
                    break
        return len(max)
            