// 98. Validate Binary Search Tree
// https://leetcode.com/problems/validate-binary-search-tree/

function TreeNode(val, left, right) {
  this.val = val === undefined ? 0 : val;
  this.left = left === undefined ? null : left;
  this.right = right === undefined ? null : right;
}

/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isValidBST = function (root) {
  return checkBST(root, null, null);
};

const checkBST = (node, lowerLimit, upperLimit) => {
  let result = true;

  if (node.left) result = result && checkBST(node.left, lowerLimit, node.val);
  if (node.right) result = result && checkBST(node.right, node.val, upperLimit);

  if (lowerLimit !== null) result = result && lowerLimit < node.val;
  if (upperLimit !== null) result = result && node.val < upperLimit;

  return result;
};
