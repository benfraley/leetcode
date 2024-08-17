class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        if len(strs) == 0: return prefix
        strs = list(set(strs)) # removes duplicates
        if len(strs) == 1: return strs[0]
        strs.sort(key=len) # sets the first item to the shortest str
        for i in range(1, len(strs[0])+1):
            for s in strs:
                if strs[0][:i] != s[:i]:
                    return prefix
            prefix = strs[0][:i] 
        return prefix