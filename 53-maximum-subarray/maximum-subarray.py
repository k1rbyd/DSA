class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = float('-inf')
        current = 0
        for i in range(n):
            current = max(nums[i], current + nums[i])
            ans = max(ans, current)
        return ans