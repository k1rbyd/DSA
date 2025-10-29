class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        nums = [0] * n
        for i in range(n):
            nums[i] = start + (2*i)
        result = 0
        for i in nums:
            result ^= i
        return result