# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        d1 = ListNode(0)
        d2 = ListNode(0)
        prev1 = d1
        prev2 = d2

        while head:
            if head.val < x:
                prev1.next = head
                prev1 = prev1.next
            else:
                prev2.next = head
                prev2 = prev2.next
            head = head.next
        
        prev2.next = None
        prev1.next = d2.next
        return d1.next