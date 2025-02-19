// 437. Path Sum III
// https://leetcode.com/problems/path-sum-iii/

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
    public int pathSum(TreeNode root, int targetSum) {
        if (root == null)
            return 0;

        return this.calculatePathSum(root, targetSum, false);
    }

    public int calculatePathSum(TreeNode node, long targetSum, boolean isAdding) {
        int count = 0;

        if (targetSum == node.val)
            count += 1;

        if (node.left != null) {
            if (!isAdding)
                count += this.calculatePathSum(node.left, targetSum, false);

            count += this.calculatePathSum(node.left, targetSum - node.val, true);
        }

        if (node.right != null) {
            if (!isAdding)
                count += this.calculatePathSum(node.right, targetSum, false);

            count += this.calculatePathSum(node.right, targetSum - node.val, true);
        }

        return count;
    }
}