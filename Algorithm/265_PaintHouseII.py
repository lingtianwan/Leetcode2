# There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.
#
# The cost of painting each house with a certain color is represented by a n x k cost matrix. For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on... Find the minimum cost to paint all houses.
#
# Note:
# All costs are positive integers.
#
# Follow up:
# Could you solve it in O(nk) runtime?


class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        n = len(costs)
        if n == 0:
            return 0
        k = len(costs[0])
        if k == 1:
            return min(costs[:][0])
        dp = [[0 for x in range(k)] for y in range(n)]
        for i in range(k):
            dp[0][i] = costs[0][i]
        for i in range(1, n):
            for j in range(k):
                dp[i][j] = min(dp[i-1][:j] + dp[i-1][j + 1:]) + costs[i][j]
        return min(dp[-1])
