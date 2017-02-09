# Given two sparse matrices A and B, return the result of AB.
#
# You may assume that A's column number is equal to B's row number.
#
# Example:
#
# A = [
#   [ 1, 0, 0],
#   [-1, 0, 3]
# ]
#
# B = [
#   [ 7, 0, 0 ],
#   [ 0, 0, 0 ],
#   [ 0, 0, 1 ]
# ]
#
#
#      |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
# AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
#                   | 0 0 1 |


class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(A)
        n = len(B)
        if m * n == 0:
            return []
        q = len(B[0])
        res = [[0 for x in range(q)] for y in range(m)]
        for i in range(m):
            for j in range(n):
                if A[i][j] != 0:
                    for k in range(q):
                        res[i][k] += A[i][j] * B[j][k]
        return res
