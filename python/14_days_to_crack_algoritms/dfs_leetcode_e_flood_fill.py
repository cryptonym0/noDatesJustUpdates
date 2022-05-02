# https://leetcode.com/submissions/detail/682859230/
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # image is the graph
        # sr is the y axis
        # sc is the x axis
        # we can repreent this like image[sr][sc] = starting node
        # new colour, is really just the change that is going to happen for all nodes that:
        # A. Have the same value of the starting node AND
        # B. Are not seperated by another colour

        rows = len(image)
        cols = len(image[0])
        init_state = image[sr][sc]

        visited_set = set()
        self.dfs(visited_set, image, sr, sc, init_state, newColor)
        return image

    def dfs(self, visited_set, image, row, col, initial_colour, target_colour):
        curr_row = 0 <= row < len(image)
        curr_col = 0 <= col < len(image[0])

        if not curr_row or not curr_col:
            return

        if (row, col) in visited_set:
            return

        if image[row][col] != initial_colour:
            return

        # do the search
        visited_set.add((row, col))
        image[row][col] = target_colour

        # the 4 ways
        self.dfs(visited_set, image, row + 1, col, initial_colour, target_colour)
        self.dfs(visited_set, image, row - 1, col, initial_colour, target_colour)
        self.dfs(visited_set, image, row, col + 1, initial_colour, target_colour)
        self.dfs(visited_set, image, row, col - 1, initial_colour, target_colour)