# https://leetcode.com/submissions/detail/667760051/


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # naieve: slice and reattach v slow
        # SC O(n) and TC O(n)
        # total_length = len(nums)
        # index_to_split = k % total_length
        # pointer = total_length - index_to_split
        # nums[:] = nums[pointer:] + nums[:pointer]

        # use reverse method() v fast
        # SC O(n) and TC O(n)
        k = k % len(nums)
        nums.reverse()
        nums[0:k] = reversed(nums[0:k])
        nums[k:] = reversed(nums[k:])
