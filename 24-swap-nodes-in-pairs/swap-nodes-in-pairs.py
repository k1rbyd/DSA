# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head == None:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        start = dummy
        left = dummy
        right = dummy
        while left.next != None and left.next.next != None:
            left = start.next
            right = start.next.next
            start.next = right
            left.next = right.next
            right.next = left
            start = left
        return dummy.next