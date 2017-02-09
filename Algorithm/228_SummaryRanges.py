# Given a sorted integer array without duplicates, return the summary of its ranges.
#
# For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].


class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0:
            return []
        res = []
        start = 0
        nums.append(nums[-1] + 2)
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] != 1:
                if i - 1 == start:
                    res.append(str(nums[i - 1]))
                else:
                    res.append(str(nums[start]) + '->' + str(nums[i - 1]))
                start = i
        return res
