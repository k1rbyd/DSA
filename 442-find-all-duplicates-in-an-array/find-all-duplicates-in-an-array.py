class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        check = set([])
        res = []
        nums.sort()
        for num in nums:
            if num in check:
                res.append(num)
            else:
                check.add(num)
        return res