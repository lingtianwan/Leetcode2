# Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.
#
# Note: The input string may contain letters other than the parentheses ( and ).
#
# Examples:
# "()())()" -> ["()()()", "(())()"]
# "(a)())()" -> ["(a)()()", "(a())()"]
# ")(" -> [""]


class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def dfs(s):
            mi = calc(s)
            if mi == 0:
                return [s]
            ans = []
            for i in range(len(s)):
                if s[i] in ('(', ')'):
                    ns = s[:i] + s[i+1:]
                    if ns not in visited and calc(ns) < mi:
                        visited.add(ns)
                        ans.extend(dfs(ns))
            return ans

        def calc(s):
            maps = {'(': 1, ')': -1}
            a = 0
            b = 0
            for c in s:
                a += maps.get(c, 0)
                if a < 0:
                    b += 1
                a = max(a, 0)
            return a + b

        visited = set([s])
        return dfs(s)
