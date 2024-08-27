# https://leetcode.com/problems/substring-with-concatenation-of-all-words/
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words or not s:
            return []
        words.sort() # sort for comparison
        ret = set() # store unique indices
        left = 0
        p_len = len(words) * len(words[0]) # length of possible permutations
        x = len(words[0]) # length of a word
        right = len(s)-p_len

        while left <= right:
            # slide window from large to small
            lword = s[left:left+p_len]
            rword = s[right:right+p_len]
            
            # break the right and left words into x sized pieces, compare to words
            llist = sorted([lword[i:i+x] for i in range(0, len(lword), x)])
            rlist = sorted([rword[i:i+x] for i in range(0, len(rword), x)])
            if llist == words:
                ret.add(left)
            if rlist == words:
                ret.add(right)
            left += 1
            right -= 1
        return sorted(list(ret))