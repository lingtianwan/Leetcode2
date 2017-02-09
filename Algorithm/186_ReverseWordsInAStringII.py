# Given an input string, reverse the string word by word. A word is defined as a sequence of non-space characters.
#
# The input string does not contain leading or trailing spaces and the words are always separated by a single space.
#
# For example,
# Given s = "the sky is blue",
# return "blue is sky the".
#
# Could you do it in-place without allocating extra space?


class Solution:
    # @param s, a list of 1 length strings, e.g., s = ['h','e','l','l','o']
    # @return nothing
    def reverseWords(self, s):
        idx = 0
        s.append(' ')
        for i in range(len(s)):
            if s[i] == ' ':
                s[idx:i] = reversed(s[idx:i])
                idx = i + 1
        del s[-1]
        s.reverse()
