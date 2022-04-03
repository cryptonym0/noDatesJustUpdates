# https://leetcode.com/submissions/detail/669976840/
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        # Format: (lambda x: x + 1)(some argument to pass)
        lambda_func = lambda x: prod(x) - sum(x)
        num_list = list(map(int, str(n)))
        return (lambda_func)(num_list)
