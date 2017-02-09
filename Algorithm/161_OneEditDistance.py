# Given two strings S and T, determine if they are both one edit distance apart.


class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == t:
            return False
        m = len(s)
        n = len(t)
        if m * n == 0 and m + n == 1:
            return True
        if abs(m - n) > 1:
            return False
        if m == n:
            change = 0
            for i in range(m):
                if s[i] != t[i]:
                    change += 1
                    if change > 1:
                        return False
        elif m > n:
            change = 0
            i = j = 0
            while j < n:
                if s[i] != t[j]:
                    change += 1
                    i += 1
                else:
                    i += 1
                    j += 1
                if change > 1:
                    return False
        else:
            change = 0
            i = j = 0
            while i < m:
                if s[i] != t[j]:
                    change += 1
                    j += 1
                else:
                    i += 1
                    j += 1
                if change > 1:
                    return False
        return True
