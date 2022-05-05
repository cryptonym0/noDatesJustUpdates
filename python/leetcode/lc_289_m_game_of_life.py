import numpy as np


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # count # of neighbours that are 0 or 1
        # determine next state based on counts
        # live is 1
        def ck(x, y, n, m, b):
            cnt = 0
            rg = [-1, 0, 1]
            for i, j in product(rg, rg):
                if i == j == 0:
                    continue
                xx, yy = x + i, y + j
                if 0 <= xx < n and 0 <= yy < m:
                    cnt += b[xx][yy]
            return cnt

        n, m = len(board), len(board[0])
        board2 = deepcopy(board)
        for i in range(n):
            for j in range(m):
                cnt = ck(i, j, n, m, board2)
                if board2[i][j]:
                    if cnt in [2, 3]:
                        board[i][j] = 1
                    else:
                        board[i][j] = 0
                elif ck(i, j, n, m, board2) == 3:
                    board[i][j] = 1
