# https://leetcode.com/submissions/detail/669406257/
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
        # s = s[::-1]
        # slicer = slice(None, None, -1)
        # s = s[slicer]
