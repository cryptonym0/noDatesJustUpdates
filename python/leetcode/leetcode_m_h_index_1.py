# https://leetcode.com/submissions/detail/670212761/
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # naiever itterative
        # sort in order
        # keep highest number, removed and number of elements that are greater than 0
        # compare current_hightst_total_greater_than_0 to last_hightst_total_greater_than_0
        # if current is less than last, return last
        # h index cannot be greater than the number of papers.

        # 1. Sort list to be in order
        citations.sort(reverse=True)
        max_c = 0
        for index, value in enumerate(citations):
            if index + 1 <= value:
                max_c += 1
            else:
                break
        return max_c
