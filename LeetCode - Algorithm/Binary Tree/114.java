// 114. Flatten Binary Tree to Linked List
// https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

import java.util.Stack;

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
    public void flatten1(TreeNode root) {
        if (root == null)
            return;

        Stack<TreeNode> stack = new Stack<>();

        stack.add(root);

        while (!stack.isEmpty()) {
            TreeNode node = stack.pop();

            if (node.right != null)
                stack.add(node.right);
            if (node.left != null)
                stack.add(node.left);

            node.left = null;
            if (!stack.isEmpty())
                node.right = stack.peek();
        }
    }

    public void flatten2(TreeNode root) {
        if (root == null)
            return;

        TreeNode left = root.left;
        TreeNode right = root.right;

        this.flatten2(left);
        this.flatten2(right);

        root.left = null;
        root.right = left;

        TreeNode current = root;
        while (current.right != null)
            current = current.right;
        current.right = right;
    }
}
