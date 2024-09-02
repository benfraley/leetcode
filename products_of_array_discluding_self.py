# https://neetcode.io/problems/products-of-array-discluding-self
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        import maths
        ret = []
        for i, n in enumerate(nums):
            temp = nums[:]
            temp[i] = 1
            ret.append(math.prod(temp))

        return ret