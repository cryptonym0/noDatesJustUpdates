# https://leetcode.com/submissions/detail/667723926/
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x)[::-1] == str(x):
            return True
        return False
