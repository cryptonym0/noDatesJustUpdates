# https://leetcode.com/submissions/detail/669410428/
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()

        for i in range(len(s)):
            s[i] = s[i][::-1]

        return " ".join(s)

        s = s.split()
