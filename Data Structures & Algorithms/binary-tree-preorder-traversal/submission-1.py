# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        nodes = []
        def preorder(node):
            if not node:
                return
            
            preorder(node.right)
            preorder(node.left)
            nodes.append(node.val)
        
        preorder(root)
        nodes.reverse()
        return nodes