# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c in ('(', '[', '{'):
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                out = stack.pop()
                if out + c not in ('()', '{}', '[]'):
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
