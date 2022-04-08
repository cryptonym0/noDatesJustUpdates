# https://leetcode.com/submissions/detail/674500323/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # in order, get all nodes. OH ez peasy!
        io_list = []
        down_left = True
        current_node = None

        while root:
            # if down
            if down_left:
                # check left
                if root.left:
                    # reverse links
                    temp = root.left
                    root.left = current_node
                    current_node = root
                    root = temp
                # else right
                else:
                    root.left = current_node
                    down_left = False
            # else back up
            else:
                io_list.append(root.val)
                if root.right:
                    current_node = root.left
                    root = root.right
                    down_left = True
                else:
                    root = root.left
        return io_list
