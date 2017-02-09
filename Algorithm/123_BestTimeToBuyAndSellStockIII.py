# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete at most two transactions.
#
# Note:
# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 0:
            return 0
        f1 = [0 for x in range(n)]
        f2 = [0 for x in range(n)]
        min_val = prices[0]
        for i in range(1, n):
            min_val = min(min_val, prices[i])
            f1[i] = max(f1[i-1], prices[i] - min_val)
        max_val = prices[n - 1]
        for j in range(n - 2, -1, -1):
            max_val = max(max_val, prices[j])
            f2[j] = max(f2[j+1], max_val - prices[j])
        res = 0
        for i in range(n):
            res = max(res, f1[i] + f2[i])
        return res
