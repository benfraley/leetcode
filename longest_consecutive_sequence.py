# https://neetcode.io/problems/longest-consecutive-sequence
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        sequences = []
        for n in nums:
            if n-1 in nums:
                continue
            else: # beginning of a sequence
                slen = 1
                while True:
                    if n + slen in nums:
                        slen +=1
                    else:
                        break
                sequences.append(slen)
        return max(sequences)