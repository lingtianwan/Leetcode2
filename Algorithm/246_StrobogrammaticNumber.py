# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
#
# Write a function to determine if a number is strobogrammatic. The number is represented as a string.
#
# For example, the numbers "69", "88", and "818" are all strobogrammatic.


class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        rot = {'1':'1', '6':'9', '8':'8', '9':'6', '0':'0'}
        res = ''
        for c in num:
            if c not in rot:
                return False
            res += rot[c]
        if num == res[::-1]:
            return True
        return False
