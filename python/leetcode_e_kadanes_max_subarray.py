# https://leetcode.com/submissions/detail/667780602/
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #Kadane's algorithm O(n) O(1)
        local_max = nums[0]
        global_max = nums[0]
        
        for i in range(1, len(nums)):
            current_index = nums[i]
            local_max = max(local_max + current_index, current_index) 
            global_max  = max(local_max, global_max )
            
        return global_max 
        
        # Kadane's algorithm local_maximum at index i is the maximum of arr[i] and the sum of arr[i] and local_maximum at index i-1.
