#https://leetcode.com/problems/integer-to-roman/submissions/
class Solution:
    def intToRoman(self, num: int) -> str:
        my_str = ""  
        key_map = {
          1000: "M",
          900: "CM",
          500: "D",
          400: "CD",
          100: "C",
          90: "XC",
          50: "L",
          40: "XL",
          10: "X",
          9: "IX",
          5: "V",
          4: "IV",
          1: "I"
        }

        for key, value in key_map.items():
          while num >= key:
            my_str += value
            num -= key
        return my_str
        
#Runtime: 75 ms, faster than 46.63% of Python3 online submissions for Integer to Roman.
#Memory Usage: 13.9 MB, less than 85.61% of Python3 online submissions for Integer to Roman.
