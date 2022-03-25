#https://leetcode.com/problems/roman-to-integer/submissions/

class Solution:
    def romanToInt(self, s: str) -> int:
        #start with hashmap
        my_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        sum = 0
        #itterate through my string
        for i in range(len(s)):
            #check for out of bounds
            if i + 1 < len(s) and my_dict[s[i]] < my_dict[s[i+1]]:
                    sum -= my_dict[s[i]]
            else:
                sum += my_dict[s[i]]
        return sum
    
#Runtime: 52 ms, faster than 83.11% of Python3 online submissions for Roman to Integer.
#Memory Usage: 13.8 MB, less than 81.75% of Python3 online submissions for Roman to Integer.        
        
