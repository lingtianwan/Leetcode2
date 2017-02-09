# The count-and-say sequence is the sequence of integers beginning as follows:
# 1, 11, 21, 1211, 111221, ...
#
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# Given an integer n, generate the nth sequence.
#
# Note: The sequence of integers will be represented as a string.


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        start = '1'
        for i in range(n-1):
            cur = start[0]
            cnt = 1
            res = ''
            for j in range(1, len(start)):
                if start[j] == cur:
                    cnt += 1
                else:
                    res += str(cnt) + cur
                    cur = start[j]
                    cnt = 1
            res += str(cnt) + cur
            start = res
        return start
