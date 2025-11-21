class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        check = set([])
        res = set([])
        nums.sort()
        for num in nums:
            if num in check:
                res.add(num)
            else:
                check.add(num)
        return list(res)