// 110. Balanced Binary Tree
// https://leetcode.com/problems/balanced-binary-tree/

/**
 * @param {TreeNode} root
 * @return {boolean}
 */

// Depth First Search (DFS) // Recursive Function
// time complexity: O(2nlogn) = O(nlogn) || space complexity: O(1)
var isBalanced = function (root) {
  if (!root) return true;

  return (
    Math.abs(getHeight(root.left) - getHeight(root.right)) < 2 &&
    isBalanced(root.left) &&
    isBalanced(root.right)
  );
};

var getHeight = (root) => {
  if (!root) return 0;

  const left = 1 + getHeight(root.left);
  const right = 1 + getHeight(root.right);

  return Math.max(left, right);
};

function TreeNode(val, left, right) {
  this.val = val === undefined ? 0 : val;
  this.left = left === undefined ? null : left;
  this.right = right === undefined ? null : right;
}
