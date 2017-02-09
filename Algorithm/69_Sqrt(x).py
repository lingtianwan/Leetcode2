# Implement int sqrt(int x).
#
# Compute and return the square root of x.


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        low = 0
        high = x
        mid = x / 2
        while low <= high:
            if mid ** 2 == x:
                return mid
            elif mid ** 2 < x:
                low = mid + 1
            else:
                high = mid - 1
            mid = (low + high) / 2
        return mid
