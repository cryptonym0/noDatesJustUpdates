# https://leetcode.com/submissions/detail/667904365/
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = {}
        underscore_count = 0
        for index, value in enumerate(nums):
            if seen.get(value, None) is not None:
                underscore_count += 1
                continue
            else:
                seen[value] = index

        nums.clear()
        for key in seen:
            nums.append(key)
        for i in range(underscore_count):
            nums.append(None)

        #         print(k)
        #         print(underscore_count)
        #         k = len(nums) - underscore_count
        return len(nums) - underscore_count
