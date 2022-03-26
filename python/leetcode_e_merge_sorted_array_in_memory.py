# https://leetcode.com/submissions/detail/667743939/
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        limit = m + n
        
        if limit == 0 or limit == m:
            return None
        
        #assigon pointers
        arr_cursor = limit-1
        m_pointer = m-1
        n_pointer = n-1
        
        #loop
        while m_pointer >=0 and n_pointer >=0:
            #if m > n
            if nums1[m_pointer] > nums2[n_pointer]:
                nums1[arr_cursor] = nums1[m_pointer]
                arr_cursor -=1
                m_pointer -= 1
                # self.fill_slot(nums1, nums1, m_pointer, arr_cursor)
            #else m < n
            else:
                nums1[arr_cursor] = nums2[n_pointer]
                arr_cursor -=1
                n_pointer -= 1
        
        #fill remaining
        while m_pointer >= 0:
            nums1[arr_cursor] = nums1[m_pointer]
            arr_cursor -=1
            m_pointer -= 1
        while n_pointer >= 0:
            nums1[arr_cursor] = nums2[n_pointer]
            arr_cursor -=1
            n_pointer -= 1
            
    #TOO SLOW BUT W.E.
    def fill_slot(self, target_arr: List[int], num_arr: List[int], pointer: int, cursor: int):
        target_arr[cursor] = num_arr[pointer]
        cursor -=1
        pointer -= 1
