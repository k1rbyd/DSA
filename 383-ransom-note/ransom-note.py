class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        a1 = [0] * 26
        a2 = [0] * 26
        for i in ransomNote:
            a1[ord(i) - 97] += 1
        for i in magazine:
            a2[ord(i) -97] += 1
        for i in range(26):
            if a2[i]<a1[i]:
                return False
        return True