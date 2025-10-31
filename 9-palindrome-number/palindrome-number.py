class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        temp = x
        check = 0
        while temp!=0:
            check *= 10
            check += (temp%10)
            temp /= 10
        return check==x
        