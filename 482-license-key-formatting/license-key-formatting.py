class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = s.replace("-", "")
        s = list(s)
        i = len(s)
        while i > k:
            i -= k
            s.insert(i, "-")

        return "".join(s).upper()