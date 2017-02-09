# This is a follow up of Shortest Word Distance. The only difference is now word1 could be the same as word2.
#
# Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.
#
# word1 and word2 may be the same and they represent two individual words in the list.
#
# For example,
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
#
# Given word1 = “makes”, word2 = “coding”, return 1.
# Given word1 = "makes", word2 = "makes", return 3.
#
# Note:
# You may assume word1 and word2 are both in the list.


class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
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
                elif (start_word == word1 and word == word2) or (start_word == word2 and word == word1):
                    min_val = min(min_val, i - start_idx)
                    start_word = word
                start_idx = i
        return min_val
