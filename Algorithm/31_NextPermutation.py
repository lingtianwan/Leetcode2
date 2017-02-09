# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
#
# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
#
# The replacement must be in-place, do not allocate extra memory.
#
# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1:
            return
        partition = -1
        for i in range(n - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                partition = i - 1
                break
        if partition == -1:
            nums.reverse()
            return
        end = n - 1
        for i in range(n - 1, partition, -1):
            if nums[i] > nums[partition]:
                end = i
                break
        nums[end], nums[partition] = nums[partition], nums[end]
        for i in range(partition + 1, (n + partition + 1) / 2):
            nums[i], nums[n + partition - i] = nums[n + partition - i], nums[i]
        return
