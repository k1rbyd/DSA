# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        start = head
        result = 0
        while start:
            result *= 2
            if start.val == 1:
                result += 1
            start = start.next
        return result