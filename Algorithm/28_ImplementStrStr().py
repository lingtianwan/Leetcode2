# Implement strStr().
#
# Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':
            return 0
        start = 0
        n = len(needle)
        for i in range(len(haystack) - n + 1):
            if haystack[i] == needle[0]:
                start = i
                same = True
                for j in range(n):
                    if haystack[i+j] != needle[j]:
                        same = False
                if same == True:
                    return i
        return -1
