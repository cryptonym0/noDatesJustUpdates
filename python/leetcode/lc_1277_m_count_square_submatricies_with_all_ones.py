class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        # dynamic programming: remembering stuff to save time later.
        total_rows = len(matrix)
        total_cols = len(matrix[0])
        return_value = 0

        for row in range(total_rows):
            for col in range(total_cols):
                if matrix[row][col] != 0 and row != 0 and col != 0:
                    north = matrix[row - 1][col]
                    west = matrix[row][col - 1]
                    diagonal_nw = matrix[row - 1][col - 1]
                    matrix[row][col] = min(north, west, diagonal_nw) + 1
                return_value += matrix[row][col]
        return return_value
