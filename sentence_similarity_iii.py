# https://leetcode.com/problems/sentence-similarity-iii/?envType=daily-question&envId=2024-10-06
# medium difficulty
class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        long = sentence1
        short = sentence2
        if len(long) < len(short):
            long, short = short, long
        long = long.split(" ")
        short = short.split(" ")
        l, r = 0, len(long)-1
        while len(short) > 0:
            #print(long, short)
            if long[0] == short[0]:
                long.pop(0)
                short.pop(0)
            elif long[-1] == short[-1]:
                long.pop(-1)
                short.pop(-1)
            else:
                return False
        return True
