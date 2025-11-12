class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        out = 0
        res = 0
        for i in range(len(gain)):
            out += gain[i]
            if out>res:
                res = out
        return res