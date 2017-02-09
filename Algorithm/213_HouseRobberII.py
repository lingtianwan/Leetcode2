# Note: This is an extension of House Robber.
#
# After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not get too much attention. This time, all houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, the security system for these houses remain the same as for those in the previous street.
#
# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        if n <= 2:
            return max(nums)
        dp1 = [0 for _ in range(n)]
        dp2 = [0 for _ in range(n)]
        dp1[1] = nums[0]
        dp2[1] = nums[1]
        for i in range(2, n):
            dp1[i] = max(dp1[i - 1], (dp1[i - 2] + nums[i - 1]))
            dp2[i] = max(dp2[i - 1], (dp2[i - 2] + nums[i]))
        return max(dp1[-1], dp2[-1])
