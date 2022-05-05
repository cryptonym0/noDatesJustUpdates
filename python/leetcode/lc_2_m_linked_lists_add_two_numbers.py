# https://leetcode.com/submissions/detail/676020282/
# Time is O(n) where n is the length of the longest list.
# Space is O(1) - i think....

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # 2 + 5 = 7
        # 40 + 60 + 7 = 107
        # 300 + 400 + 107 = 807
        # ok need a 3rd list to return, a pointer to read from the head and....a temp val for overflow
        rem = 0
        rtn_node = ListNode(0)
        rtn_head = rtn_node
        while l1 or l2:
            iteration_total = 0
            if l1:
                iteration_total += l1.val
                l1 = l1.next
            if l2:
                iteration_total += l2.val
                l2 = l2.next
            iteration_total += rem
            rem = iteration_total // 10
            rtn_node.next = ListNode(iteration_total % 10)
            rtn_node = rtn_node.next
        if rem != 0:
            rtn_node.next = ListNode(rem)
            rtn_node = rtn_node.next

        return rtn_head.next
