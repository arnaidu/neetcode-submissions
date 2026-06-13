# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0, True
            
            left_height, isLeftBalanced = dfs(node.left)
            right_height, isRightBalanced = dfs(node.right)

            if not isLeftBalanced or not isRightBalanced:
                return 0, False

            diff = abs(left_height - right_height)
            if diff > 1:
                return 0, False

            height_parent = 1 + max(left_height, right_height)
            return height_parent, True
        return dfs(root)[1]