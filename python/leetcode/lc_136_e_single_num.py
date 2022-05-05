class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # use bit manipulation to find duplicates...
        length = len(nums)
        for i in range(1, length):
            nums[0] ^= nums[i]
        return nums[0]
