class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            else:
                if not stack: 
                    return False
                if (i==')' and stack.pop()=='(') or (i=='}' and stack.pop()=='{') or (i==']' and stack.pop()=='['):
                    continue
                else:
                    return False
        if len(stack)==0:
            return True
        return False
        