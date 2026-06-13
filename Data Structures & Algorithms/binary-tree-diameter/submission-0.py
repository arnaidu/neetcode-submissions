class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0, 0  # height, diameter

            left_height, left_diameter = dfs(node.left)
            right_height, right_diameter = dfs(node.right)

            height = 1 + max(left_height, right_height)

            diameter_through_node = left_height + right_height

            diameter = max(
                left_diameter,
                right_diameter,
                diameter_through_node
            )

            return height, diameter

        _, diameter = dfs(root)
        return diameter
