class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        # lets split k into 2 dimensions
        y_shift = (k // n) % m
        x_shift = k % n
        rtn_mtx = []

        if x_shift == 0 and y_shift == 0:
            return grid

        if x_shift > 0:
            carry = [0]
            for i, j in enumerate(grid):
                rtn_mtx.append(carry + grid[i][:-x_shift])
                carry = grid[i][-x_shift:]
            rtn_mtx[0] = carry + grid[0][:-x_shift]
        else:
            rtn_mtx = grid

        return rtn_mtx[-y_shift:] + rtn_mtx[:-y_shift]
