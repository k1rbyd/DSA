# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head == None:
            return None
        
        temp = head
        after = temp.next
        before = None
        ans = ListNode(0)
        ans.next = before
        while temp:
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        return before