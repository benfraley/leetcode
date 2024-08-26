# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        vals = len(nums)
        for i in range(1, len(nums)-1):
            if nums[i-1] == nums[i] and nums[i] == nums[i+1]: # compare three elements
                nums[i-1] = "_" # change first element in compare to string
                vals -= 1 # each time we 'remove' a value we decrease this by one
        nums.sort(key=sort_key) # inline sort putting integers first
        return vals

def sort_key(x): # i had to look up how custom sorts work
    if isinstance(x, int): 
        return (0,x) # ints go first
    else:
        return (1, x) # strings go second