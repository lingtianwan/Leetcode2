# Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
#
#     For example, given array S = {-1 2 1 -4}, and target = 1.
#
#     The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        min_sums = 2147483648
        max_sums = -2147483647
        n = len(nums)
        for i in range(0, n - 2):
            if i and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = n - 1
            while left < right:
                tmp = nums[i] + nums[left] + nums[right]
                if tmp == target:
                    return target
                elif tmp < target:
                    max_sums = max(max_sums, tmp)
                    left += 1
                else:
                    min_sums = min(min_sums, tmp)
                    right -= 1
        if abs(target - min_sums) > abs(target - max_sums):
            return max_sums
        else:
            return min_sums
