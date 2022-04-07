# https://leetcode.com/submissions/detail/675392716/

class Solution: #naieve - optimized
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            x = stones.pop(stones.index(max(stones)))
            y = stones.pop(stones.index(max(stones)))
            if x != y:
                stones.append(abs(x-y))
        if stones:    
            return stones[0]
        return 0
                
                
# import heapq
# class Solution: #heap me
#     def lastStoneWeight(self, stones: List[int]) -> int:
#         s = [-i for i in stones]
#         heapq.heapify(s)
#         while len(s) > 1:
#             x, y = heapq.heappop(s), heapq.heappop(s)
#             heapq.heappush(s, -abs(x - y))
#         return abs(s[0])
    
# class Solution: #naieve
#     def lastStoneWeight(self, stones: List[int]) -> int:
#         while len(stones) > 1:
#             x = stones.pop(stones.index(max(stones)))
#             y = stones.pop(stones.index(max(stones)))
            
#             if x != y:
#                 stones.append(max(x,y) - min(x,y))
#         if stones:    
#             return stones[0]
#         return 0
