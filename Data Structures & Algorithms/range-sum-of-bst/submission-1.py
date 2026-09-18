# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def traverse(low, high, node):
            if not node:
                return 0

            total = 0
            if low <= node.val <= high:
                total += node.val
            
            # if we go left, then the current node.val is now upper bound
            # therefore, if it is less than low, then we can't have any other nodes
            # so if it is greater than or equal to low, then we have more nodes possibly
            if node.val >= low:
                total += traverse(low, high, node.left)
            
            # vice versa if less than or equal to high, then we have more nodes possibly
            if node.val <= high:
                total += traverse(low, high, node.right)
            
            return total

        return traverse(low, high, root)