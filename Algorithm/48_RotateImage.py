# You are given an n x n 2D matrix representing an image.
#
# Rotate the image by 90 degrees (clockwise).
#
# Follow up:
# Could you do this in-place?


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n <= 1:
            return
        start = 0
        end = n - 1
        while n > 1:
            for i in range(0, end - start):
                matrix[start+i][end], matrix[end][end-i], matrix[end-i][start], matrix[start][start+i] = matrix[start][start+i], matrix[start+i][end], matrix[end][end-i], matrix[end-i][start]
            start += 1
            end -= 1
            n -= 2
        return
