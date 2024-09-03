# https://neetcode.io/problems/two-integer-sum-ii
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) -1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1] # 1-indexed solution
            elif numbers[l] + numbers[r] > target: # bigger than the target, so reduce the right pointer
                r -= 1
            elif numbers[l] + numbers[r] < target: # less than the target, so increase the left pointer
                l += 1