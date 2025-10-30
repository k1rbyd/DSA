class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans = {}
        for i, num in enumerate(nums):
            num2 = target - num
            if num2 in ans:
                return [ans[num2], i]
            ans[num] = i
        return -1