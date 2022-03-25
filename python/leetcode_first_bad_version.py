# https://leetcode.com/problems/first-bad-version/submissions/
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # if n == 1:
        #     return n
        high = n
        low = 0
        # mid = 0

        # binary search kinda
        while low <= high:
            mid = (low + high )//2

            # if bad
            if isBadVersion(mid):
                # if not first bad:
                if isBadVersion(mid - 1):
                    high = mid - 1
                # if first bad!:
                else:
                    return mid
            else:
                low = mid + 1

# Runtime: 43 ms, faster than 49.75% of Python3 online submissions for First Bad Version.
# Memory Usage: 13.9 MB, less than 67.69% of Python3 online submissions for First Bad Version.