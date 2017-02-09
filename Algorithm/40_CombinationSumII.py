# Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
#
# Each number in C may only be used once in the combination.
#
# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,
# A solution set is:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(candidates) == 0:
            return []
        res = []
        def dfs(cand, sums, sol_list):
            if sums == 0:
                res.append(sol_list)
                return
            elif sums > 0:
                i = 0
                while i < len(cand):
                    dfs(cand[i+1:], sums - cand[i], sol_list + [cand[i]])
                    while i + 1 < len(cand) and cand[i] == cand[i + 1]:
                        i += 1
                    i += 1
        candidates.sort()
        dfs(candidates, target, [])
        return res
