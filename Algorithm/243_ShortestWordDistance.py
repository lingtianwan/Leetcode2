# Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.
#
# For example,
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
#
# Given word1 = “coding”, word2 = “practice”, return 3.
# Given word1 = "makes", word2 = "coding", return 1.
#
# Note:
# You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.


class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        min_val = len(words)
        start_idx = 0
        start_word = None
        for i, word in enumerate(words):
            if word in (word1, word2):
                if start_word is None:
                    start_word = word
                elif word != start_word:
                    min_val = min(min_val, i - start_idx)
                    start_word = word
                start_idx = i
        return min_val
