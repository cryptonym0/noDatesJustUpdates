# https://leetcode.com/submissions/detail/667793488/


class Solution:
    def average(self, salary: List[int]) -> float:
        last = len(salary) - 1
        salary.sort()

        salary.pop(last)
        salary.pop(0)

        return sum(salary) / len(salary)
