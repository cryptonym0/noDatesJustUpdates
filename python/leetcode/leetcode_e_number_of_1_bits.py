# https://leetcode.com/submissions/detail/669970370/
class Solution:
    def hammingWeight(self, n: int) -> int:
        c = "{:032b}".format(n).count("1")
        return c
