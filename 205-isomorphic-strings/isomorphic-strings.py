class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_to_t = {}
        t_to_s = {}
        for s_char, t_char in zip(s, t):
            if s_char in s_to_t:
                if s_to_t[s_char] != t_char:
                    return False
            else:
                if t_char in t_to_s:
                    return False
                s_to_t[s_char] = t_char
                t_to_s[t_char] = s_char

        return True