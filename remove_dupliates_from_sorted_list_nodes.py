# https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# runtime 72.93%, memory 29.5%
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current:
            while current.next != None and current.val == current.next.val:
                current.next = current.next.next
            current = current.next
        return head
        