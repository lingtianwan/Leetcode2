# Given numRows, generate the first numRows of Pascal's triangle.
#
# For example, given numRows = 5,
# Return
#
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        for i in range(numRows):
            row = [1]
            if i > 0:
                for j in range(1, i):
                    row.append(res[i - 1][j - 1] + res[i - 1][j])
                row.append(1)
            res.append(row)
        return res
