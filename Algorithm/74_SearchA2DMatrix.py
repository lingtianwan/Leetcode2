# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
#
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
# For example,
#
# Consider the following matrix:
#
# [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# Given target = 3, return true.


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        low = 0
        high = m - 1
        while low + 1 < high:
            mid = (low + high) / 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                low = mid
            else:
                high = mid
        if matrix[high][0] == target or matrix[low][0] == target:
            return True
        if matrix[high][0] < target:
            row = high
        else:
            row = low
        left = 0
        right = n - 1
        while left < right:
            mid = (left + right) / 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if matrix[row][left] == target:
            return True
        else:
            return False
