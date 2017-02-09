# Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.
#
# For example, given
# s = "leetcode",
# dict = ["leet", "code"].
#
# Return true because "leetcode" can be segmented as "leet code".


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        n = len(s)
        if n == 0:
            return False
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for word in wordDict:
                size = len(word)
                if i - size >= 0 and word == s[(i - size):i]:
                    dp[i] |= dp[i - size]
        return dp[-1]
