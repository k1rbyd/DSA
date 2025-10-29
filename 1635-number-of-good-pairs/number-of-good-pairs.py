class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        i = 0
        j = 0
        n = len(nums)
        while i<n:
            for j in range(i,n):
                if nums[i]==nums[j] and i!=j:
                    count += 1
            i += 1
        return count