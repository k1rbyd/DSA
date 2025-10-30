class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = {}
        for i,num in enumerate(nums):
            if num in result:
                result[num] += 1
            else:
                result[num] = 1
        return max(result, key=result.get)
