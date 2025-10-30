class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        a1 = [0] * 26
        a2 = [0] * 26
        for i in s:
            a1[ord(i)-97] += 1
        for i in t:
            a2[ord(i)-97] += 1
        return (a1==a2)