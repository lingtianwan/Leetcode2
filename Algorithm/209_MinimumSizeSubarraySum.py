# Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of which the sum ≥ s. If there isn't one, return 0 instead.
#
# For example, given the array [2,3,1,2,4,3] and s = 7,
# the subarray [4,3] has the minimal length under the problem constraint.
#
# click to show more practice.
#
# More practice:
# If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).


class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        start = 0
        end = 0
        ans = n + 1
        sums = 0
        while end < n:
            while end < n and sums < s:
                sums += nums[end]
                end += 1
            while start < end and sums >= s:
                ans = min(ans, end - start)
                sums -= nums[start]
                start += 1
        if ans > n:
            return 0
        return ans
