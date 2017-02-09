# Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
#
# Solve it without division and in O(n).
#
# For example, given [1,2,3,4], return [24,12,8,6].
#
# Follow up:
# Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        p = 1
        for num in nums:
            output.append(p)
            p *= num
        p = 1
        for i, num in enumerate(nums[::-1]):
            output[-1-i] *= p
            p *= num
        return output
