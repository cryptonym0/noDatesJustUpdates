# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        odd_pointer, even_pointer = head, head.next
        odd_head, even_head = odd_pointer, even_pointer

        while even_pointer and even_pointer.next:
            odd_pointer.next = odd_pointer.next.next
            even_pointer.next = even_pointer.next.next
            odd_pointer = odd_pointer.next
            even_pointer = even_pointer.next

        odd_pointer.next = even_head
        return odd_head
