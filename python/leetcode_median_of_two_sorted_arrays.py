# https://leetcode.com/submissions/detail/667820282/
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        limit = m + n
        merged_arr = [None] * limit
        mid = limit//2
        
        # assign pointers
        arr_cursor = limit-1
        m -= 1
        n -= 1
        
        #loop
        while m >=0 and n >=0:
            #if m > n
            if nums1[m] > nums2[n]:
                merged_arr[arr_cursor] = nums1[m]
                arr_cursor -=1
                m -=1
            #if m < n
            else:
                merged_arr[arr_cursor] = nums2[n]
                arr_cursor -=1
                n -=1
                
        #fill remaining if different lengths
        while m >=0:
            merged_arr[arr_cursor] = nums1[m]
            arr_cursor -=1
            m -=1
        while n >=0:
            merged_arr[arr_cursor] = nums2[n]
            arr_cursor -=1
            n -=1
            
        #median
        if len(merged_arr)%2 != 0:
            return(merged_arr[mid])
        return(float(merged_arr[mid] + merged_arr[mid-1])/2)
