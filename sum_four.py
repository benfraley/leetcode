class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        quads = set()
        for i in range(len(nums)):
            j = i + 1 # check the next element in the list
            k = len(nums) -1 # check the last element in list
            while j < k:
                # get fourth number via binary search
                sub_nums = nums[j+1:k-1]
                for l, val in enumerate(sub_nums):
                    total = nums[i] + nums[j] + nums[k] + nums[l+j+1]
                    print(i,j,k,l)
                    print(nums[i],nums[j],nums[k],nums[l])
                    print(total)
                    if total == target:
                        quads.add((nums[i], nums[j], nums[k], nums[l+j+1]))
                    elif total < target:
                        l += 1
                    else:
                        break
                if total == target:
                    j += 1
                    k -= 1
                elif total < target:
                    j += 1 # move to the right
                elif total > target:
                    k -= 1 # move to the left
        return list(quads)