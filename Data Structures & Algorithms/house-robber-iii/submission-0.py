# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0, 0

            left_robbed, left_skipped = dfs(node.left)
            right_robbed, right_skipped = dfs(node.right)

            # amount if we rob current house and skip left and right
            robbed = node.val + left_skipped + right_skipped

            skipped = max(left_robbed, left_skipped) + max(right_robbed, right_skipped)
            return robbed, skipped
        
        return max(dfs(root))