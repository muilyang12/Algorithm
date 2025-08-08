// 230. Kth Smallest Element in a BST
// https://leetcode.com/problems/kth-smallest-element-in-a-bst/

function TreeNode(val, left, right) {
  this.val = val === undefined ? 0 : val;
  this.left = left === undefined ? null : left;
  this.right = right === undefined ? null : right;
}

/**
 * @param {TreeNode} root
 * @param {number} k
 * @return {number}
 */
var kthSmallest = function (root, k) {
  const values = [];

  getValues(root, values, k);

  return values[k - 1];
};

const getValues = (node, values, target) => {
  if (!node) return;

  if (values.length >= target) return;

  getValues(node.left, values, target);

  if (values.length >= target) return;

  values.push(node.val);

  if (values.length >= target) return;

  getValues(node.right, values, target);
};
