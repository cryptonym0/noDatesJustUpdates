# https://leetcode.com/submissions/detail/667791407/


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # both numbers odd
        # first number odd second even
        # first number even second odd
        # both even
        if low % 2 == 0:
            low += 1
        if high % 2 == 0:
            high -= 1
        return (high - low) // 2 + 1
