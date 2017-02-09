# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
#
# Example 1:
#
# 11110
# 11010
# 11000
# 00000
# Answer: 1
#
# Example 2:
#
# 11000
# 11000
# 00100
# 00011
# Answer: 3


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        visited = [[False for x in range(n)] for y in range(m)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    ans += 1
                    self.bsf(grid, visited, i, j, m, n)
        return ans

    def bsf(self, grid, visited, x, y, m, n):
        dz = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        queue = [(x, y)]
        visited[x][y] = True
        while queue:
            front = queue.pop(0)
            for p in dz:
                np = [(front[0] + p[0]), (front[1] + p[1])]
                if self.isValid(np, m, n) and grid[np[0]][np[1]] == '1' and not visited[np[0]][np[1]]:
                    visited[np[0]][np[1]] = True
                    queue.append(np)
        return

    def isValid(self, np, m, n):
        return np[0] >= 0 and np[0] < m and np[1] >= 0 and np[1] < n
