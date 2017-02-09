# Design a data structure that supports the following two operations:
#
# void addWord(word)
# bool search(word)
# search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.
#
# For example:
#
# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true
# Note:
# You may assume that all words are consist of lowercase letters a-z.


class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.wordlist = collections.defaultdict(set)


    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        self.wordlist[len(word)].add(word)

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if '.' not in word:
            for elem in self.wordlist.get(len(word), ()):
                if word == elem:
                    return True
            return False
        for elem in self.wordlist.get(len(word), ()):
            find = True
            for i in range(len(word)):
                if word[i] != elem[i] and word[i] != '.':
                    find = False
                    break
            if find:
                return True
        return False


# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")
