# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
#
# Example:
#
# Input: "babad"
#
# Output: "bab"
#
# Note: "aba" is also a valid answer.
# Example:
#
# Input: "cbbd"
#
# Output: "bb"


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        for i in range(len(s)):
            pa1 = self.findLongestPalindrome(s, i, i)
            if len(pa1) > len(res):
                res = pa1
            pa2 = self.findLongestPalindrome(s, i, i+1)
            if len(pa2) > len(res):
                res = pa2
        return res

    def findLongestPalindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]
