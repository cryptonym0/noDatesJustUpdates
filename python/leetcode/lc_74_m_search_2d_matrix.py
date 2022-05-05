# https://leetcode.com/submissions/detail/670024757/


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nr, nc = len(matrix), len(matrix[0])
        l, r = 0, nr * nc - 1
        while r >= l:
            m = (l + r) // 2
            v = matrix[m // nc][m % nc]
            if v == target:
                return True
            elif v > target:
                r = m - 1
            else:
                l = m + 1
        return False

        # too slow :(


#         mbot, mtop = -1, len(matrix)
#         row_end = len(matrix[0])-1
#         print(mbot)
#         print(mtop)

#         while mtop - mbot > 1:
#             mmid = (mbot + mtop) // 2
#             if matrix[mmid][0] >= target and matrix[mmid][row_end] >= target:
#                 print("Here: ", mmid)
#                 rbot, rtop = -1, row_end+1
#                 #round 2
#                 while rtop - rbot > 1:
#                     rmid = (rtop + rbot) // 2
#                     if matrix[mmid][rmid] == target:
#                         return true
#                     if matrix[mmid][rmid] > target:
#                         rtop == rmid
#                     else:
#                         rbot == rmid

#                 return False

#             if matrix[mmid][0] < target:
#                 mbot = mmid
#             else:
#                 mtop = mmid
#         return False
