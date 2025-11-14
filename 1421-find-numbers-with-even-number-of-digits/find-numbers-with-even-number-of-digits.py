class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0

        for num in nums:
            temp = 0
            while num!=0:
                temp += 1
                num /= 10
            if temp%2==0:
                count += 1
        return count