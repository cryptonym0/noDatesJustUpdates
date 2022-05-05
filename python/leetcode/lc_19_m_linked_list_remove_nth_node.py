# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        l, r = head, head
        if not r.next:
            return None
        for i in range(n):
            r = r.next

        if not r:  # if r is none that means we should remove last element from the end
            return head.next

        while r.next:
            r = r.next
            l = l.next  # 1 previous of what we should remove
        l.next = l.next.next

        return head
