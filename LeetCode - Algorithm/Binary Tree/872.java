// 872. Leaf-Similar Trees
// https://leetcode.com/problems/leaf-similar-trees/

import java.util.ArrayList;
import java.util.List;

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
    public boolean leafSimilar(TreeNode root1, TreeNode root2) {
        List<Integer> leafValues1 = new ArrayList<>();
        List<Integer> leafValues2 = new ArrayList<>();

        this.collectLeafs(root1, leafValues1);
        this.collectLeafs(root2, leafValues2);

        return leafValues1.equals(leafValues2);
    }

    public void collectLeafs(TreeNode node, List<Integer> leafValues) {
        if (node == null) {
            return;
        }

        if (node.left == null && node.right == null) {
            leafValues.add(node.val);

            return;
        }

        collectLeafs(node.left, leafValues);
        collectLeafs(node.right, leafValues);

    }
}