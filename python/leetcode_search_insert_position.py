# https://leetcode.com/problems/search-insert-position/submissions/


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # binary search again
        low = 0
        high = len(nums) - 1
        mid = 0

        while low <= high:
            mid = (low + high) // 2

            # if found:
            if nums[mid] == target:
                return mid

            # if higher:
            elif nums[mid] > target:
                high = mid - 1

            # if lower:
            else:
                low = mid + 1
        return low


# Runtime: 44 ms, faster than 98.61% of Python3 online submissions for Search Insert Position.
# Memory Usage: 14.7 MB, less than 86.59% of Python3 online submissions for Search Insert Position.
