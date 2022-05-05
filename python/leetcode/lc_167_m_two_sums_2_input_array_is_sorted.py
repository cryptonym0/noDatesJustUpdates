# https://leetcode.com/submissions/detail/669402993/
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen_numbers = {}
        for index, value in enumerate(numbers):
            potential_value = target - value
            if seen_numbers.get(potential_value, None) is not None:
                # if seen_numbers.get(potential_value) is not index:
                return [seen_numbers.get(potential_value) + 1, index + 1]
            seen_numbers[value] = index
        return None
