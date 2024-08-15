class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        triplets = set()
        for i in range(len(nums)):
            j = i + 1 # check the next element in the list
            k = len(nums) -1 # check the last element in list
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    triplets.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif total < 0:
                    j += 1 # move to the right
                elif total > 0:
                    k -= 1 # move to the left
        return list(triplets)
        