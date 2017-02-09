# A message containing letters from A-Z is being encoded to numbers using the following mapping:
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given an encoded message containing digits, determine the total number of ways to decode it.
#
# For example,
# Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).
#
# The number of ways decoding "12" is 2.


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0:
            return 0
        if n == 1:
            if int(s[0]) > 0:
                return 1
            else:
                return 0
        dp = [0] * (n + 1)
        dp[0] = 1
        if int(s[0]) > 0:
            dp[1] = 1
        for i in range(1, n):
            if int(s[i]) > 0:
                dp[i+1] += dp[i]
            if int(s[i-1:i+1]) in range(10, 27):
                dp[i+1] += dp[i-1]
        return dp[n]
