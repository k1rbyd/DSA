class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        total = 0
        count = 0
        prefix = {0: 1}

        for num in nums:
            total += num
            if (total - k) in prefix:
                count += prefix[total - k]
            prefix[total] = prefix.get(total, 0) + 1

        return count