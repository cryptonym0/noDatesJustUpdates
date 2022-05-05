# https://leetcode.com/submissions/detail/669398351/
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        index = 0
        list_len = len(nums)

        while index < list_len - 1:
            list_len = len(nums)
            print("index:", index)
            print("list len:", list_len - 1)
            # if 0
            if nums[index] == 0:
                count += 1
                nums.pop(index)
            # else not 0
            else:
                index += 1
        for i in range(0, count):
            nums.append(0)
