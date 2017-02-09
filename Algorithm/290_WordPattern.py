# Given a pattern and a string str, find if str follows the same pattern.
#
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.
#
# Examples:
# pattern = "abba", str = "dog cat cat dog" should return true.
# pattern = "abba", str = "dog cat cat fish" should return false.
# pattern = "aaaa", str = "dog cat cat dog" should return false.
# pattern = "abba", str = "dog dog dog dog" should return false.
# Notes:
# You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.


class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        pat_map = {}
        str_map = {}
        str_list = str.split(' ')
        if len(pattern) != len(str_list):
            return False
        for i in range(len(pattern)):
            if (pattern[i] not in pat_map) and (str_list[i] not in str_map):
                pat_map[pattern[i]] = str_list[i]
                str_map[str_list[i]] = pattern[i]
                continue
            elif (pat_map.get(pattern[i], '') == str_list[i]) and (str_map.get(str_list[i], '') == pattern[i]):
                continue
            else:
                return False
        return True
