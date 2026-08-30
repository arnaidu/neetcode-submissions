# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        visible_nodes = []
        seen = set()
        def traverse(node: Optional[TreeNode], visible_nodes: List[int], curr_height: int, heights_seen: set[int]):
            # given current height, if we have seen visible_node, then
            # move right, if not then move left
            # value moving right first so we get right most first
            # moving left is valid if new height
            if not node:
                return

            if curr_height not in heights_seen:
                visible_nodes.append(node.val)
            
            # we have seen height so track
            heights_seen.add(curr_height)
            next_height = curr_height + 1

            if node.right:
                traverse(node.right, visible_nodes, next_height, heights_seen)
            if node.left:
                traverse(node.left, visible_nodes, next_height, heights_seen)
        
        traverse(root, visible_nodes, 1, seen)
        return visible_nodes

        
