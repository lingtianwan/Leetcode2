# Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).
#
# Example 1:
# Input: [3, 2, 1]
#
# Output: 1
#
# Explanation: The third maximum is 1.
# Example 2:
# Input: [1, 2]
#
# Output: 2
#
# Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
# Example 3:
# Input: [2, 2, 3, 1]
#
# Output: 1
#
# Explanation: Note that the third maximum here means the third maximum distinct number.
# Both numbers with value 2 are both considered as second maximum.


class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1 = max2 = max3 = None
        for i in nums:
            if max1 is None or i > max1:
                max1, max2, max3 = i, max1, max2
            elif (max2 is None or i > max2) and i != max1:
                max2, max3 = i, max2
            elif (max3 is None or i > max3) and i != max2 and i != max1:
                max3 = i
        if max3 is None:
            return max1
        return max3
