# Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.
#
# Example 1:
# Given words = ["bat", "tab", "cat"]
# Return [[0, 1], [1, 0]]
# The palindromes are ["battab", "tabbat"]
# Example 2:
# Given words = ["abcd", "dcba", "lls", "s", "sssll"]
# Return [[0, 1], [1, 0], [3, 2], [2, 4]]
# The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]


class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        maps = {y:x for x, y in enumerate(words)}
        res = set()
        for i, word in enumerate(words):
            if '' in maps and word != '' and self.isPalindrome(word):
                res.add((maps[''], i))
                res.add((i, maps['']))
            if word[::-1] in maps and maps[word[::-1]] != i:
                res.add((i, maps[word[::-1]]))
                res.add((maps[word[::-1]], i))
            for k in range(len(word)):
                left = word[:k]
                right = word[k:]
                if self.isPalindrome(left) and right[::-1] in maps and i != maps[right[::-1]]:
                    res.add((maps[right[::-1]], i))
                if self.isPalindrome(right) and left[::-1] in maps and i != maps[left[::-1]]:
                    res.add((i, maps[left[::-1]]))
        return list(res)

    def isPalindrome(self, word):
        return word == word[::-1]
