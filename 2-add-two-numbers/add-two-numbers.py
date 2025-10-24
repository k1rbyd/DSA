# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        start1 = l1
        start2 = l2
        carry = 0
        prev = None
        while start1 and start2:
            temp = start1.val + start2.val + carry
            if temp > 9:
                temp -= 10
                carry = 1
            else:
                carry = 0
            start1.val = temp
            prev = start1
            start1 = start1.next
            start2 = start2.next

        if start2:
            prev.next = start2
            start1 = start2

        while start1:
            temp = start1.val + carry
            if temp > 9:
                temp -= 10
                carry = 1
            else:
                carry = 0
            start1.val = temp
            prev = start1
            start1 = start1.next

        if carry:
            prev.next = ListNode(1)

        return l1