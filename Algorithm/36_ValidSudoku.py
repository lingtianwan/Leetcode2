# Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
#
# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
#
#
# A partially filled sudoku which is valid.
#
# Note:
# A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row = [set() for i in range(9)]
        col = [set() for i in range(9)]
        sqr = [[set() for i in range(3)] for j in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in row[i]:
                    return False
                row[i].add(board[i][j])
                if board[i][j] in col[j]:
                    return False
                col[j].add(board[i][j])
                if board[i][j] in sqr[i/3][j/3]:
                    return False
                sqr[i/3][j/3].add(board[i][j])
        return True
