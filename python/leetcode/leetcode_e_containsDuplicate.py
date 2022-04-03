# https://leetcode.com/submissions/detail/667775084/
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen_dict = {}
        for index, value in enumerate(nums):
            # if seen return true
            if seen_dict.get(value, None) is not None:
                return True
            # else add to dict
            seen_dict[value] = value

        # return false
        return False
