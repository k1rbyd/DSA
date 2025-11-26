class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        seen = set()
        res = set()
        n = len(s)

        for i in range(n - 9):
            sub = s[i:i+10]

            if sub in seen:
                res.add(sub)
            else:
                seen.add(sub)

        return list(res)