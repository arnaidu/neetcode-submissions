# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        def traverse(node: Optional[TreeNode]) -> int:
            nonlocal count
            nonlocal k

            if not node:
                return None

            # go left
            value = traverse(node.left)

            if value is not None:
                return value

            # at root
            count += 1

            # check if we hit k
            if count == k:
                return node.val

            # go right
            value = traverse(node.right)

            if value is not None:
                return value

        return traverse(root)
