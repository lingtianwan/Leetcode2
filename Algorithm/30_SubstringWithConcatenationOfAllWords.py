# You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.
#
# For example, given:
# s: "barfoothefoobarman"
# words: ["foo", "bar"]
#
# You should return the indices: [0,9].
# (order does not matter).


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(words) == 0 or len(s) == 0 or len(words[0]) == 0:
            return []
        n = len(words[0])
        m = len(words)
        res = []
        word_map = collections.Counter(words)
        for i in range(n):
            sub_map = collections.defaultdict(int)
            cnt = 0
            left = i
            for j in range(i, len(s) - n + 1, n):
                cur = s[j:j+n]
                if cur in word_map:
                    sub_map[cur] += 1
                    cnt += 1
                    while sub_map[cur] > word_map[cur]:
                        sub_map[s[left:left+n]] -= 1
                        cnt -= 1
                        left += n
                    if cnt == m:
                        res.append(left)
                else:
                    sub_map = collections.defaultdict(int)
                    cnt = 0
                    left = j + n
        return res
