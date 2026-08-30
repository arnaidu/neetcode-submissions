# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        curr_max = root.val
        num_good_nodes = 0
        def traverse(node: Optional[TreeNode], curr_max: int):
            nonlocal num_good_nodes

            if not node:
                return
            
            # if this is a good_node
            if node.val >= curr_max:
                num_good_nodes += 1

            # search left
            traverse(node.left, max(node.val, curr_max))
            # search right
            traverse(node.right, max(node.val, curr_max))

        traverse(root, root.val)

        return num_good_nodes
        