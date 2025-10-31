class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        left = 0

        ans = -1
        i = 0
        while i<len(nums):
            right = total - left - nums[i]
            if left==right:
                return i
            left += nums[i]
            i += 1
        return ans