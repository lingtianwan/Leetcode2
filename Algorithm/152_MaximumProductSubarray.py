# Find the contiguous subarray within an array (containing at least one number) which has the largest product.
#
# For example, given the array [2,3,-2,4],
# the contiguous subarray [2,3] has the largest product = 6.


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        pos = [0 for x in range(n)]
        neg = [0 for x in range(n)]
        pos[0] = nums[0]
        neg[0] = nums[0]
        res = nums[0]
        for i in range(1, n):
            pos[i] = max(max(pos[i-1]*nums[i], neg[i-1]*nums[i]), nums[i])
            neg[i] = min(min(pos[i-1]*nums[i], neg[i-1]*nums[i]), nums[i])
            res = max(res, pos[i])
        return res
