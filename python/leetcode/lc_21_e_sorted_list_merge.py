# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # merge sort
        # return list(merge(list1, list2)) # didnt work

        # naieve
        head = ListNode()
        tail = head
        # both lists exist
        while list1 and list2:
            # list 1 smaller val
            if list1.val < list2.val:
                tail.next = list1  # add node to tail
                list1 = list1.next  # new head
            # list 2 smaller val
            else:
                tail.next = list2  # add node to tail
                list2 = list2.next  # new head
            tail = tail.next

        # list 1 exists, list2 does not
        if list1:
            tail.next = list1
        # list1 DNE, list2 Exits
        elif list2:
            tail.next = list2
        return head.next
