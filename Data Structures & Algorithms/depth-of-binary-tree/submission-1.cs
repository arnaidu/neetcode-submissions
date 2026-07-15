/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

public class Solution {
    public int MaxDepth(TreeNode root) {
        return dfs(root);
    }

    public int dfs(TreeNode node) {
        if (node is null) {
            return 0;
        }

        int left = 0;
        int right = 0;
        if (node.left is not null) {
            left = dfs(node.left);
        }

        if (node.right is not null) {
            right = dfs(node.right);
        }

        return 1 + Math.Max(left, right);
    }
}
