# https://leetcode.com/problems/sort-array-by-increasing-frequency/
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        from collections import Counter, OrderedDict
        counter, ret = OrderedDict(sorted(Counter(nums).items(), key=lambda item:(item[1], -item[0]))), []
        for k, v in counter.items():
            ret.extend([k] * v)
        return ret
