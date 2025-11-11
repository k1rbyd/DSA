class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s) 
        i = 0
        n = len(s)

        for j in range(n + 1):
            if j == n or s[j] == ' ':
                left, right = i, j - 1
                while left < right:
                    s[left], s[right] = s[right], s[left]
                    left += 1
                    right -= 1
                i = j + 1  

        return ''.join(s) 