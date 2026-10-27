# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:       
        def find_node_to_delete_and_parent(node, key):
            parent = None
            while node and node.val != key:
                parent = node
                if key > node.val:
                    node = node.right
                else:
                    node = node.left
            return (parent, node)
        
        parent, node = find_node_to_delete_and_parent(root, key)
        
        if not node:
            return root

        def two_children(parent, node):
            successor_parent = node
            successor = node.right
            while successor.left:
                successor_parent = successor
                successor = successor.left
            
            node.val = successor.val
            if successor_parent == node:
                successor_parent.right = successor.right
            else:
                successor_parent.left = successor.right


        if node.left and node.right:
            # find smallest node in right subtree
            two_children(parent, node)
            return root
        
        # Case 2: Node has zero or one child
        child = node.left if node.left else node.right

        if not parent:
            return child
        elif parent.left == node:
            parent.left = child
        else:
            parent.right = child

        return root
            

        
