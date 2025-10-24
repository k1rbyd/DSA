class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        ans=0
        for person in accounts:
            wealth=sum(person)
            if wealth>ans:
                ans=wealth
        return ans