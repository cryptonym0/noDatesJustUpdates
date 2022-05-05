# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left, right = head, head
        toggle = False
        while right.next:
            right = right.next
            if toggle:
                left = left.next
            toggle = not toggle
        return left.next if toggle else left
