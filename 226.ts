// 226. Invert Binary Tree
// https://leetcode.com/problems/invert-binary-tree/

// Divide-and-conquer
// // time complexity: O(n) || space complexity: O(n) => Depth of stack
function invertTree1(root: TreeNode | null): TreeNode | null {
  if (root === null) return root;
  if (root.left === null && root.right === null) return root;

  const temp = root.left;
  root.left = root.right;
  root.right = temp;

  invertTree1(root.left);
  invertTree1(root.right);

  return root;
}

class TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;
    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
      this.val = val === undefined ? 0 : val;
      this.left = left === undefined ? null : left;
      this.right = right === undefined ? null : right;
    }
  }
