# https://leetcode.com/submissions/detail/667809161/
class Solution:
    @lru_cache(None) #too slow w/o this
    def tribonacci(self, n: int) -> int:
        if n == 2:
            return 1
        if n < 2:
            return n
        return self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
