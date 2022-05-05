# https://leetcode.com/submissions/detail/674043752/
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # volume = l x h
        # index is x, value is y
        # height = [1,8,6,2,5,4,8,3,7]
        # But really it's more like: [ (0,1),(1,8),(2,6),(3,2),(4,5),(5,4),(6,8)(7,3),(8,3),(9,7)]
        # brute force, naieve too slow!!
        #         max_vol = 0
        #         n = len(height)
        #         # Area = length of shorter vertical line * distance between line
        # area = lambda l, d : l * d
        #         for i in range(0, n-1):
        #             for j in range(1, n):
        #                 new_h = area(min(height[i], height[j]), j - i)
        #                 max_vol = max(new_h, max_vol)
        #         return max_vol

        # 2 pointers
        left = 0
        right = len(height) - 1
        max_vol = 0
        area = lambda l, d: l * d

        while left < right:
            new_h = area(min(height[left], height[right]), (right - left))
            max_vol = max(new_h, max_vol)

            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                left += 1
                right -= 1
        return max_vol
