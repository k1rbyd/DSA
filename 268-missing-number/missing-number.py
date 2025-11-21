class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        totalsum = (n * (n + 1) // 2)
        return totalsum - sum(nums)

#        n = len(nums)
#        for i in range(0,n+1):
#            if i in nums:
#                continue
#            else:
#                return i
