# https://leetcode.com/submissions/detail/670227120/
from collections import defaultdict


class Solution:
    def minDeletions(self, s: str) -> int:
        freq = defaultdict(int)
        freq_count = set()
        deletions = 0

        for char in s:
            freq[char] += 1

        for item in freq.values():
            while item in freq_count:
                item -= 1
                deletions += 1
            if item:
                freq_count.add(item)
        return deletions
