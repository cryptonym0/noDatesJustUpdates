class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # for i in range(0, len(nums)+1):
        #     if i not in nums:
        #         return i
        length = len(nums)
        res = 0
        for i in range(len(nums)):
            res ^= nums[i]
        for i in range(len(nums) + 1):
            res ^= i
        return res
