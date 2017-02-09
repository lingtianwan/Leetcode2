# Rotate an array of n elements to the right by k steps.
#
# For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
#
# Note:
# Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
#
# [show hint]
#
# Hint:
# Could you do it in-place with O(1) extra space?
# Related problem: Reverse Words in a String II


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        for i in range(n / 2):
            nums[i], nums[n-i-1] = nums[n-i-1], nums[i]
        for i in range(k / 2):
            nums[i], nums[k-i-1] = nums[k-i-1], nums[i]
        for i in range(k, (n+k)/2):
            nums[i], nums[n-1-i+k] = nums[n-1-i+k], nums[i]
        return
