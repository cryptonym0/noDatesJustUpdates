# https://leetcode.com/submissions/detail/674474259/

from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # hashtable default dict containing count of letters
        seen = defaultdict(int)
        to_do = defaultdict(int)
        n = len(s1)
        m = len(s2)
        first_index = 0

        # fill my first 2 hashmaps of equal length
        for i in s1:
            seen[i] += 1
        # use substring of s2, length of s1
        for j in s2[0:n]:
            to_do[j] += 1

        #         for i, j in zip(s1, s2[0:n]):
        #             seen[i] += 1
        #             to_do[j] += 1

        # check if same....
        if seen == to_do:
            return True

        # itterate, sliding window
        for i in range(n, m):
            to_do[s2[i]] += 1  # slide over one
            to_do[s2[first_index]] -= 1  # pop first element off

            # delete all keys that are 0
            if to_do[s2[first_index]] <= 0:
                to_do.pop(s2[first_index])

            if seen == to_do:
                return True
            first_index += 1
        return False
