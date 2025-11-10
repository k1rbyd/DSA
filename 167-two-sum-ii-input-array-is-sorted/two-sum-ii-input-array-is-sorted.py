class Solution(object):
    def twoSum(self, nums, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = {}
        for i, num in enumerate(nums):
            num2 = target - num
            if num2 in res:
                return [res[num2]+1, i+1]
            res[num] = i
        return -1