# https://leetcode.com/problems/two-city-scheduling/submissions/
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # interviewing 2n ppl
        # lowest cost
        sum = 0
        num_each_city = len(costs) // 2
        costs = sorted(costs, key=lambda a: a[0] - a[1])

        # 2 loops?
        for item in costs[:num_each_city]:
            sum += item[0]

        for item in costs[num_each_city:]:
            sum += item[1]

        return sum


# Runtime: 40 ms, faster than 93.32% of Python3 online submissions for Two City Scheduling.
# Memory Usage: 14 MB, less than 43.95% of Python3 online submissions for Two City Scheduling.
