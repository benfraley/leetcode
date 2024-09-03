# https://neetcode.io/problems/three-integer-sum
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []

        for l, n in enumerate(nums):
            if l > 0 and l < len(nums) - 2 and n == nums[l-1]:
                continue
            m, r = l + 1, len(nums) - 1
            while m < r:
                print(l,m,r)
                total = nums[l] + nums[m] + nums[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    m +=1
                else:
                    triplets.append([nums[l], nums[m], nums[r]])
                    m += 1
                    while m < r and nums[m] == nums[m-1]:
                        m += 1
        return triplets