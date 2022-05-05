class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # if n == 2:
        #     return False
        # return n and not (n & n - 1)
        i = 0
        while 4 ** i <= n:
            if 4 ** i == n:
                return True
            i += 1
        return False
