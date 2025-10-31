class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        number = 0
        for i in digits:
            number *= 10
            number += i
        number +=1
        ans = []
        while number!=0:
            x = (number % 10)
            ans.insert(0,x)
            number /= 10
        return ans