from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        # use a dequeue
        seen_deque = deque()
        seen_deque.append(root)

        while seen_deque:
            node = seen_deque.popleft()
            if not node and seen_deque:
                return not any(seen_deque)
            elif node:
                seen_deque.append(node.left)
                seen_deque.append(node.right)

        return True
