# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        elif not root or not subRoot:
            return False

        def same(node, subRoot):
            if not node and not subRoot:
                return True
            elif not node or not subRoot:
                return False
            
            return node.val == subRoot.val and same(node.left, subRoot.left) and same(node.right, subRoot.right)
       
        return same(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


