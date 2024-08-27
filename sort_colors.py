# https://leetcode.com/problems/sort-colors/
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ret = []
        length = len(nums)
        cur = nums[:]
        for i in range(3):
            for k in cur:
                if i == k:
                    nums.append(i)
        for _ in range(length):
            nums.pop(0)
