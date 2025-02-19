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

/*
 * In Java, the 'int' type can store values ranging from -2,147,483,648 to
 * 2,147,483,647 (Roughly -2 × 10^9 to 2 × 10^9).
 * 
 * In this problem, the constraints for a node's value is -10^9 <= Node.val <=
 * 10^9, meaning that adding or subtracting just two or three such values can
 * exceed the 'int' range. Therefore, I need to use the 'long' type for this
 * problem. I must be cautious when performing arithmetic operations in Java and
 * check the constraints.
 */