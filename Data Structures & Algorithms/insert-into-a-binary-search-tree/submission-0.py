# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node_to_insert = TreeNode(val) 
        if not root:
            return node_to_insert
        
        parent = root
        while True:
            if val > parent.val:
                if not parent.right:
                    parent.right = node_to_insert
                    break
                parent = parent.right
            elif val < parent.val:
                if not parent.left:
                    parent.left = node_to_insert
                    break
                parent = parent.left
        
        return root
            

            


