class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        check = set([])
        for num in nums:
            if num not in check:
                check.add(num)
            else:
                return num