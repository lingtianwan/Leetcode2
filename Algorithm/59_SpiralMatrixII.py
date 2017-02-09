# Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
#
# For example,
# Given n = 3,
#
# You should return the following matrix:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0 for x in range(n)] for y in range(n)]
        i = j = 0
        di = 0
        dj = 1
        for k in range(n * n):
            res[i][j] = k + 1
            if res[(i + di) % n][(j + dj) % n]:
                di, dj = dj, -di
            i += di
            j += dj
        return res
