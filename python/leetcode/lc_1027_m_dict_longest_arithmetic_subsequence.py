from collections import defaultdict


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        seen_dict = defaultdict(int)
        for i in range(1, len(nums)):
            for j in range(i):
                arithmetic_subsequence = nums[i] - nums[j]
                seen_dict[(i, arithmetic_subsequence)] = (
                    1 + seen_dict[(j, arithmetic_subsequence)]
                )
        return max(seen_dict.values()) + 1
