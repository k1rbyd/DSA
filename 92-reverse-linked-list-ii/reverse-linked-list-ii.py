# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        if left == right:
            return head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        for _ in range(left-1):
            prev = prev.next
        current = prev.next
        for _ in range(right-left):
            to_move = current.next
            current.next = to_move.next
            to_move.next = prev.next
            prev.next = to_move
        head = dummy.next
        return head