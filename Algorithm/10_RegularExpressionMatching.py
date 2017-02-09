# Implement regular expression matching with support for '.' and '*'.
#
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
#
# The matching should cover the entire input string (not partial).
#
# The function prototype should be:
# bool isMatch(const char *s, const char *p)
#
# Some examples:
# isMatch("aa","a") → false
# isMatch("aa","aa") → true
# isMatch("aaa","aa") → false
# isMatch("aa", "a*") → true
# isMatch("aa", ".*") → true
# isMatch("ab", ".*") → true
# isMatch("aab", "c*a*b") → true
# Show Company Tags
# Show Tags
# Show Similar Problems


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return self.search(s, p, 0, 0)

    def search(self, s, p, idxs, idxp):
        lens = len(s)
        lenp = len(p)
        if idxp == lenp:
            return idxs == lens
        if idxp == lenp - 1:
            return (idxs == lens - 1) and self.match(s, p, idxs, idxp)
        if p[idxp + 1] != '*':
            if idxs < lens and self.match(s, p, idxs, idxp):
                return self.search(s, p, idxs + 1, idxp + 1)
            else:
                return False
        if self.search(s, p, idxs, idxp + 2):
            return True
        for i in range(idxs, lens):
            if not self.match(s, p, i, idxp):
                return False
            if self.search(s, p, i + 1, idxp + 2):
                return True
        return False


    def match(self, s, p, idxs, idxp):
        return s[idxs] == p[idxp] or p[idxp] == '.'



class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False for i in range(len(p)+1)] for j in range(len(s)+1)]
        dp[0][0] = True
        for i in range(len(p) + 1):
            if i >= 2 and p[i-1] == '*':
                dp[0][i] = dp[0][i - 2]
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2]
                    if s[i - 1] == p[j - 2] or p[j - 2] == '.':
                        dp[i][j] |= dp[i - 1][j]
                elif p[j - 1] == '.' or s[i - 1] == p[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
        return dp[-1][-1]
