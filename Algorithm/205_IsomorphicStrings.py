# Given two strings s and t, determine if they are isomorphic.
#
# Two strings are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.
#
# For example,
# Given "egg", "add", return true.
#
# Given "foo", "bar", return false.
#
# Given "paper", "title", return true.
#
# Note:
# You may assume both s and t have the same length.


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        m = len(s)
        iso_s = {}
        iso_t = {}
        for i in range(m):
            if s[i] not in iso_s and t[i] not in iso_t:
                iso_s[s[i]] = t[i]
                iso_t[t[i]] = s[i]
            elif iso_s.get(s[i], None) != t[i] or iso_t.get(t[i], None) != s[i]:
                return False
        return True
