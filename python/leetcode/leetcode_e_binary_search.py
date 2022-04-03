# https://leetcode.com/submissions/detail/667844849/


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # actual binary search...
        bot, top = -1, len(nums)

        while top - bot > 1:
            mid = (bot + top) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                top = mid
            else:
                bot = mid
        return -1

    # def search(self, nums: List[int], target: int) -> int:
    #     #my go to for everything, way faster
    #     for index, value in enumerate(nums):
    #         if value == target:
    #             return index
    #     return -1
