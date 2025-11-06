class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        r = ""
        n = len(s)
        for i in range(n):
            if s[i].isalnum():
                r += s[i]
        return r==r[::-1]