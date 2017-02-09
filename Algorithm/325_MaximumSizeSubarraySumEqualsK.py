# Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.
#
# Note:
# The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.
#
# Example 1:
# Given nums = [1, -1, 5, -2, 3], k = 3,
# return 4. (because the subarray [1, -1, 5, -2] sums to 3 and is the longest)
#
# Example 2:
# Given nums = [-2, -1, 2, 1], k = 1,
# return 2. (because the subarray [-1, 2] sums to 1 and is the longest)
#
# Follow Up:
# Can you do it in O(n) time?
#
# Hide Company Tags


class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        maps = {0:-1}
        max_len = -2147483648
        sums = 0
        for i in range(len(nums)):
            sums += nums[i]
            if sums not in maps:
                maps[sums] = i
            if sums - k in maps:
                value = maps[sums - k]
                max_len = max(max_len, i - value)
        if max_len == -2147483648:
            return 0
        return max_len
