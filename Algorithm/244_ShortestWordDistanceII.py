# This is a follow up of Shortest Word Distance. The only difference is now you are given the list of words and your method will be called repeatedly many times with different parameters. How would you optimize it?
#
# Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list.
# 
# For example,
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
#
# Given word1 = “coding”, word2 = “practice”, return 3.
# Given word1 = "makes", word2 = "coding", return 1.
#
# Note:
# You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.


class WordDistance(object):
    def __init__(self, words):
        """
        initialize your data structure here.
        :type words: List[str]
        """
        self.dic = {}
        for i, w in enumerate(words):
            self.dic[w] = self.dic.get(w, []) + [i]
        self.max_len = len(words)

    def shortest(self, word1, word2):
        """
        Adds a word into the data structure.
        :type word1: str
        :type word2: str
        :rtype: int
        """
        i1 = i2 = 0
        distance = self.max_len
        while i1 < len(self.dic[word1]) and i2 < len(self.dic[word2]):
            distance = min(distance, abs(self.dic[word1][i1] - self.dic[word2][i2]))
            if self.dic[word1][i1] > self.dic[word2][i2]:
                i2 += 1
            else:
                i1 += 1
        return distance


# Your WordDistance object will be instantiated and called as such:
# wordDistance = WordDistance(words)
# wordDistance.shortest("word1", "word2")
# wordDistance.shortest("anotherWord1", "anotherWord2")
