# https://leetcode.com/problems/merge-sorted-array/
# runtime 92.82%, memory 88.39%
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = [] # delete everything we dont want
        nums1[m:n] = nums2[:n] # add in what we want after
        nums1.sort() # sort!
        