# Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
#
# The same repeated number may be chosen from C unlimited number of times.
#
# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# For example, given candidate set [2, 3, 6, 7] and target 7,
# A solution set is:
# [
#   [7],
#   [2, 2, 3]
# ]


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(candidates) == 0:
            return []
        res = []
        candidates.sort()
        def dfs(cand, sums, sol_list):
            if sums == 0:
                res.append(sol_list)
                return
            elif sums > 0:
                for i in range(len(cand)):
                    dfs(cand[i:], sums-cand[i], sol_list+[cand[i]])
        dfs(candidates, target, [])
        return res
