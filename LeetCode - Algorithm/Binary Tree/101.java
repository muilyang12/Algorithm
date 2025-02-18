// 101. Symmetric Tree
// https://leetcode.com/problems/symmetric-tree/

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {
    }

    TreeNode(int val) {
        this.val = val;
    }

    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    public boolean isSymmetric(TreeNode root) {
        if (root == null)
            return true;

        return compareTree(root.left, root.right);
    }

    public boolean compareTree(TreeNode root1, TreeNode root2) {
        if (root1 == null && root2 == null)
            return true;
        if (root1 == null && root2 != null)
            return false;
        if (root1 != null && root2 == null)
            return false;

        if (root1.val != root2.val)
            return false;

        return this.compareTree(root1.left, root2.right) && this.compareTree(root1.right, root2.left);
    }
}