# Given an array of strings, group anagrams together.
#
# For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Return:
#
# [
#   ["ate", "eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note: All inputs will be in lower-case.


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        lookup = {}
        for s in strs:
            key = "".join(sorted(s))
            if key in lookup:
                lookup[key].append(s)
            else:
                lookup[key] = [s]
        res = []
        for elem in lookup:
            res.append(lookup[elem])
        return res
