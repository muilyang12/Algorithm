// 104. Maximum Depth of Binary Tree
// https://leetcode.com/problems/maximum-depth-of-binary-tree/

import java.util.LinkedList;
import java.util.Queue;

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
    public int maxDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }

        int result = 0;

        Queue<TreeNode> queue = new LinkedList<>();

        queue.offer(root);

        while (!queue.isEmpty()) {
            int queueSize = queue.size();

            for (int i = 0; i < queueSize; i++) {
                TreeNode node = queue.poll();

                if (node.left != null) {
                    queue.offer(node.left);
                }

                if (node.right != null) {
                    queue.offer(node.right);
                }
            }

            result += 1;
        }

        return result;
    }
}

/*
 * In Java,
 * 
 * Set<String> hashSet = new HashSet<>();
 * 
 * Map<String, Integer> hashMap = new HashMap<>();
 * 
 * Stack<String> stack = new Stack<>();
 * 
 * Queue<String> queue = new ArrayDeque<>();
 * -> queue.offer();
 * -> queue.poll();
 * 
 * ArrayDeque<String> deque = new ArrayDeque<>();
 * -> deque.addFirst();
 * -> deque.addLast();
 * -> deque.removeFirst();
 * -> deque.removeLast();
 */