class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = []
        for i in range(n):
            pos = index[i]
            val = nums[i]
            result.insert(pos,val)
        return result