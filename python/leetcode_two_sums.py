#https://leetcode.com/problems/two-sum/submissions/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:    
        #hashmap make a list and a dict, 
        #for index, new value in ennum list,  potential value - i = new value,
        my_dict = {}
        for index, new_value in enumerate(nums):
            potential_value = target - new_value
            if my_dict.get(potential_value, None) is not None:
                if my_dict.get(potential_value) is not index: #check case 3
                    return [my_dict.get(potential_value), index]
            my_dict[new_value] = index
        return None

# Runtime: 56 ms, faster than 98.09% of Python3 online submissions for Two Sum.
# Memory Usage: 15.3 MB, less than 16.64% of Python3 online submissions for Two Sum.
        
    
        #testing cosiderations:
        # case 1: good ordered list
        # case 2: good unordered list
        # case 3: list that contains 2 or more of the same number that sum. i.e. [7,7] target = 14
        # case 4: list that contains illegal
        # unsure: does 0 count? i.e. target is 9 and the array has 9 and 0 in it
        
        #bute force: make a list, itterate through i and j, if target - i = j append both
        # brute_force_list = []
        # for i in nums:
        #     for j in nums[1:]:
        #         if target - i == j:
        #             brute_force_list.append(nums.index(i))
        #             brute_force_list.append(nums.index(j)) #break on case 3
        #             return brute_force_list
        # return brute_force_list
    
        
