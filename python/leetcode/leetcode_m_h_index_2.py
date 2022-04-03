# https://leetcode.com/submissions/detail/670213634/
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        max_c = 0
        for i, v in enumerate(citations):
            if i + 1 <= v:
                max_c += 1
            else:
                break
        return max_c
