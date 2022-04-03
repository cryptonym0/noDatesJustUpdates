# https://leetcode.com/submissions/detail/671111230/
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        # function to split the array
        low = 0
        high = sum(nums)
        rtn_sum = -1
        n = len(nums)

        # while our sum is less or equal to the max sum:
        while low <= high:
            # find the mid
            mid = low + (high - low) // 2

            # check the sum
            is_valid = True
            sum_candidate = 0
            count = 1

            for i in range(n):
                # if is summing the nums
                if nums[i] + sum_candidate <= mid:
                    sum_candidate += nums[i]

                # else is addint the count
                else:
                    count += 1
                    # count cant be greater than m,
                    if count > m or nums[i] > mid:
                        is_valid = False
                        i = n
                        continue
                    # if first number
                    sum_candidate = nums[i]

            # if mid is possible answer
            if is_valid == True:
                rtn_sum = mid
                high = mid - 1
            # else not possible -- keep itterating
            else:
                low = mid + 1
        return rtn_sum
