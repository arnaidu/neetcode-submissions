"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        order = []
        def dfs(node):
            if not node:
                return
            
            # from left to right
            for child in node.children:
                dfs(child)
            
            # no children or have exhausted the children
            order.append(node.val)

        dfs(root)
        return order

