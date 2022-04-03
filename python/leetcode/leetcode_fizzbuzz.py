# https://leetcode.com/problems/fizz-buzz/submissions/
# Runtime: 46 ms, faster than 80.02% of Python3 online submissions for Fizz Buzz.
# Memory Usage: 15.3 MB, less than 19.02% of Python3 online submissions for Fizz Buzz.


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        my_list = []
        for i in range(1, n + 1):
            my_list.append(
                "".join("Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0) or str(i))
            )
        return my_list
