# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        list1 = []
        list2 = []
        while True:
            list1.append(l1.val)
            if l1.next == None:
                break
            l1 = l1.next
        while True:
            list2.append(l2.val)
            if l2.next == None:
                break
            l2 = l2.next

        length_difference = len(list1) - len(list2)

        if length_difference > 0:
            list2.extend([0] * length_difference)
        elif length_difference < 0:
            list1.extend([0] * -length_difference)
        remainder = 0
        Lists = []
        for i in range(len(list1)):
            val = list1[i] + list2[i] + remainder
            if val >= 10:
                remainder = 1
                val = val - 10
            else:
                remainder = 0
            Lists.append(ListNode(val))

        if remainder == 1:
            Lists.append(ListNode(1))
            
        for i in range(len(Lists)):
            if (i + 1) < len(Lists):
                Lists[i].next = Lists[i+1]
        return Lists[0]