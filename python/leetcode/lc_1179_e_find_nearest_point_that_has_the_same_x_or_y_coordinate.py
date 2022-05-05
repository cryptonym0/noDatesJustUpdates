# https://leetcode.com/submissions/detail/670006290/
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        # 1 find all valid paths
        # 2 find the shorted of the valid paths
        s_man = None
        index = -1

        for i, v in enumerate(points):
            x2 = v[0]
            y2 = v[1]

            # if same return index
            if x == x2 and y == y2:
                return i
            # if valid, check if smaller than smallest known man
            if x == x2 or y == y2:
                man = abs(x - x2) + abs(y - y2)
                if s_man is None:
                    s_man = man
                    index = i
                if man < s_man:
                    s_man = man
                    index = i

        return index
