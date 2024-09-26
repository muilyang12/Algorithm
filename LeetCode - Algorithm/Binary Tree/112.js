// 112. Path Sum
// https://leetcode.com/problems/path-sum/

function TreeNode(val, left, right) {
  this.val = val === undefined ? 0 : val;
  this.left = left === undefined ? null : left;
  this.right = right === undefined ? null : right;
}

/**
 * @param {TreeNode} root
 * @param {number} targetSum
 * @return {boolean}
 */
var hasPathSum = function (root, targetSum) {
  if (!root) return false;

  if (root.val === targetSum && !root.left && !root.right) return true;

  const nextTargetSum = targetSum - root.val;

  return hasPathSum(root.left, nextTargetSum) || hasPathSum(root.right, nextTargetSum);
};
