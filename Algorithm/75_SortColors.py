# Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.
#
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
#
# Note:
# You are not suppose to use the library's sort function for this problem.
#
# click to show follow up.
#
# Follow up:
# A rather straight forward solution is a two-pass algorithm using counting sort.
# First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
#
# Could you come up with an one-pass algorithm using only constant space?


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums) - 1
        for i in range(len(nums)):
            while (nums[i] == 0 and i > left) or (nums[i] == 2 and i < right):
                if nums[i] == 0:
                    nums[i], nums[left] = nums[left], nums[i]
                    left += 1
                else:
                    nums[i], nums[right] = nums[right], nums[i]
                    right -= 1
        return
