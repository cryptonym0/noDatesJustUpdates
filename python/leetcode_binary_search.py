# https://leetcode.com/problems/binary-search/submissions/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if not exist -1
        # if exist output the index
        for index, value in enumerate(nums):
            if value == target:
                return index
        return -1

# Runtime: 252 ms, faster than 84.22% of Python3 online submissions for Binary Search.
# Memory Usage: 15.5 MB, less than 77.82% of Python3 online submissions for Binary Search.