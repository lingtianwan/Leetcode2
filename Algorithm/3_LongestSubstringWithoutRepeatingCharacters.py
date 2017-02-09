# Given a string, find the length of the longest substring without repeating characters.
#
# Examples:
#
# Given "abcabcbb", the answer is "abc", which the length is 3.
#
# Given "bbbbb", the answer is "b", with the length of 1.
#
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        maps = {}
        max_val = 0
        for i in range(len(s)):
            if s[i] not in maps:
                maps[s[i]] = i
                continue
            max_val = max(max_val, i - start)
            dup = maps[s[i]]
            for j in s[start:dup]:
                del maps[j]
            maps[s[i]] = i
            start = dup + 1
        max_val = max(max_val, len(s) - start)
        return max_val
