// 230. Kth Smallest Element in a BST
// https://leetcode.com/problems/kth-smallest-element-in-a-bst/

import java.util.List;
import java.util.ArrayList;

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
    private List<Integer> values;

    Solution() {
        this.values = new ArrayList<>();
    }

    public int kthSmallest(TreeNode root, int k) {
        this.dfsInOrder(root);

        return this.values.get(k - 1);
    }

    public void dfsInOrder(TreeNode node) {
        if (node == null)
            return;

        this.dfsInOrder(node.left);
        this.values.add(node.val);
        this.dfsInOrder(node.right);
    }
}