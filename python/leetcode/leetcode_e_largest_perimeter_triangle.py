# https://leetcode.com/submissions/detail/669988372/


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)  # big nums first
        arr_len = len(nums) + 1

        for i in range(3, arr_len):
            if nums[i - 3] < nums[i - 2] + nums[i - 1]:
                return sum(nums[i - 3 : i])
        return 0
