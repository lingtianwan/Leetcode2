# Given a 2D board and a word, find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
#
# For example,
# Given board =
#
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# word = "ABCCED", -> returns true,
# word = "SEE", -> returns true,
# word = "ABCB", -> returns false.


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if word == '':
            return True
        m = len(board)
        if m == 0:
            return False
        n = len(board[0])
        visited = [[False for x in range(n)] for y in range(m)]
        for i in range(m):
            for j in range(n):
                if word[0] == board[i][j]:
                    if self.dfs(i, j, m, n, word, board, visited):
                        return True
        return False

    def dfs(self, x, y, m, n, word, board, visited):
        if len(word) == 1:
            return True
        move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited[x][y] = True
        for dx, dy in move:
            nx = x + dx
            ny = y + dy
            if self.isValid(nx, ny, m, n):
                if (not visited[nx][ny]) and (word[1] == board[nx][ny]) and self.dfs(nx, ny, m, n, word[1:], board, visited):
                    return True
        visited[x][y] = False
        return False

    def isValid(self, x, y, m, n):
        return x >= 0 and x < m and y >= 0 and y < n
