# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         seen = {}
#         max_count = 0
#         curr_count = -1
#         index_of_last_dup = 0

#         for index, value in enumerate(s):
#             if (seen.get(value, None) is None):
#                 curr_count += 1
#                 max_count = max(max_count, curr_count)
#             elif(seen.get(value) < index_of_last_dup):
#                 curr_count += 1
#                 max_count = max(max_count, curr_count)
#             else:
#                 index_of_last_dup = index
#                 curr_count = index - index_of_last_dup
#             seen[value] = index

#         print("#", index, "\n max", max_count)


"""
Ok. So I want to say sliding window with a dictionary of seen values?
Yeah yeah lets do that
Let's start with "find if a string is unique using dict"
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result, temp, lastDup = 0, 0, 0
        unique = {}
        for index, char in enumerate(s):
            if (char not in unique) or (unique[char] < lastDup):
                temp += 1
                result = max(result, temp)
            else:
                lastDup = unique[char]
                temp = index - lastDup
            unique[char] = index
        return result
