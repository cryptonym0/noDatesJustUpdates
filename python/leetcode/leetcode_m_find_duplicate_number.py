# https://leetcode.com/submissions/detail/669381456/
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = {}
        for i, v in enumerate(nums):
            if seen.get(v, None) is not None:
                return v
            seen[v] = v
        return None
