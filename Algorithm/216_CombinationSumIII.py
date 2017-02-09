# Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
#
#
# Example 1:
#
# Input: k = 3, n = 7
#
# Output:
#
# [[1,2,4]]
#
# Example 2:
#
# Input: k = 3, n = 9
#
# Output:
#
# [[1,2,6], [1,3,5], [2,3,4]]


class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def dfs(cur, k, remain, res_list):
            if k == 0 and remain == 0:
                res.append(res_list)
                return
            if cur < 10:
                for i in range(cur + 1, 10):
                    if remain >= i and k - 1 >= 0:
                        dfs(i, k - 1, remain - i, res_list + [i])
        res = []
        dfs(0, k, n, [])
        return res
