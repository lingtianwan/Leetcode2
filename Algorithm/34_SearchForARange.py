# Given a sorted array of integers, find the starting and ending position of a given target value.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].
#
# For example,
# Given [5, 7, 7, 8, 8, 10] and target value 8,
# return [3, 4].


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = [-1, -1]
        n = len(nums)
        if n == 1 and target == nums[0]:
            return [0, 0]
        if n <= 1:
            return res
        left = 0
        right = n - 1
        while left + 1 < right:
            mid = (left + right) / 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        if nums[left] == target:
            res[0] = left
        elif nums[right] == target:
            res[0] = right
        left = 0
        right = n - 1
        while left + 1 < right:
            mid = (left + right) / 2
            if nums[mid] <= target:
                left = mid
            else:
                right = mid - 1
        if nums[right] == target:
            res[1] = right
        elif nums[left] == target:
            res[1] = left
        return res
