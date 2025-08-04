// 101. Symmetric Tree
// https://leetcode.com/problems/symmetric-tree/

function TreeNode(val, left, right) {
  this.val = val === undefined ? 0 : val;
  this.left = left === undefined ? null : left;
  this.right = right === undefined ? null : right;
}

/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isSymmetric = function (root) {
  return checkSymmetric(root.left, root.right);
};

const checkSymmetric = (left, right) => {
  if (!left && right) return false;
  else if (left && !right) return false;
  else if (!left && !right) return true;

  if (left.val !== right.val) return false;

  return checkSymmetric(left.left, right.right) && checkSymmetric(left.right, right.left);
};
