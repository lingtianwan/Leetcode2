# Given a set of distinct integers, nums, return all possible subsets.
#
# Note: The solution set must not contain duplicate subsets.
#
# For example,
# If nums = [1,2,3], a solution is:
#
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        size = len(nums)
        res = []
        def dfs(idx, num_list):
            res.append(num_list)
            for i in range(idx, size):
                dfs(i + 1, num_list + [nums[i]])
        nums.sort()
        dfs(0, [])
        return res
