# Given a sorted integer array where the range of elements are in the inclusive range [lower, upper], return its missing ranges.
#
# For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2", "4->49", "51->74", "76->99"].


class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        res = []
        nums.insert(0, lower-1)
        nums.append(upper+1)
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] < 2:
                continue
            elif nums[i + 1] - nums[i] == 2:
                res.append(str((nums[i]+nums[i+1])/2))
            else:
                res.append(str(nums[i]+1) + '->' + str(nums[i+1]-1))
        return res
