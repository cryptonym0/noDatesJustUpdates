# https://leetcode.com/submissions/detail/670217427/


class Solution:
    def sumZero(self, n: int) -> List[int]:
        # values symetrical
        # if odd, add 0
        rtn_list = []
        nums = n // 2
        for i in range(1, nums + 1):
            rtn_list.append(i)
            rtn_list.append(-i)
        if n % 2 != 0:
            rtn_list.append(0)
        return rtn_list
