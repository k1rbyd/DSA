class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        arr = [0] * n
        i = 0
        while i!=n:
            count = 0
            for j in nums:
                if nums[i]>j:
                    count += 1
            arr[i] = count
            i += 1
        return arr
        