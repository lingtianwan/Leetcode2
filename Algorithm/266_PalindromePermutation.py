# Given a string, determine if a permutation of the string could form a palindrome.
#
# For example,
# "code" -> False, "aab" -> True, "carerac" -> True.
#
# Hint:
#
# Consider the palindromes of odd vs even length. What difference do you notice?
# Count the frequency of each character.
# If each character occurs even number of times, then it must be a palindrome. How about character which occurs odd number of times?


class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cnt = collections.Counter(s)
        if len(s) % 2 == 0:
            for key, val in cnt.items():
                if val % 2 != 0:
                    return False
        else:
            single = 0
            for key, val in cnt.items():
                if val % 2 != 0:
                    single += 1
                    if single > 1:
                        return False
        return True
