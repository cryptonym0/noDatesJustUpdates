class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # i = 0
        # while(3**i <= n):
        #     if 3**i == n:
        #         return True
        #     i += 1
        # return False

        if n == 0:
            return False
        if n == 1:
            return True
        else:
            if n % 3:
                return False
            return self.isPowerOfThree(n // 3)
