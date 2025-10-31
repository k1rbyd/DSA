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
        
        result = number + 1
        ans = []
        while result!=0:
            x = (result % 10)
            ans.insert(0,x)
            result /= 10
        return ans