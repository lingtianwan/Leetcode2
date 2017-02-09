# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times. The algorithm should run in linear time and in O(1) space.
#
# Hint:
#
# How many majority elements could it possibly have?
# Do you have a better hint? Suggest it!


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num1 = None
        num2 = None
        cnt1 = 0
        cnt2 = 0
        for num in nums:
            if num == num1:
                cnt1 += 1
            elif num == num2:
                cnt2 += 1
            elif cnt1 == 0:
                num1 = num
                cnt1 += 1
            elif cnt2 == 0:
                num2 = num
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        cnt1 = 0
        cnt2 = 0
        for num in nums:
            if num == num1:
                cnt1 += 1
            if num == num2:
                cnt2 += 1
        res = []
        if cnt1 > len(nums) / 3:
            res.append(num1)
        if cnt2 > len(nums) / 3:
            res.append(num2)
        return res
