# https://leetcode.com/submissions/detail/667772878/


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # pointers
        head = 0
        tail = len(nums) - 1

        return_list = []

        while head <= tail:
            value_a = nums[head] ** 2
            value_b = nums[tail] ** 2

            if value_a < value_b:
                return_list.append(value_b)
                tail -= 1
            else:
                return_list.append(value_a)
                head += 1
        return_list.reverse()
        return return_list

        # naieve
        # #square number
        # for index, value in enumerate(nums):
        #     nums[index] = value**2
        # #sort number
        # nums.sort()
        # return nums
