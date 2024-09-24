// 226. Invert Binary Tree
// https://leetcode.com/problems/invert-binary-tree/

function TreeNode(val, left, right) {
  this.val = val === undefined ? 0 : val;
  this.left = left === undefined ? null : left;
  this.right = right === undefined ? null : right;
}

/**
 * @param {TreeNode} node
 * @return {void}
 */
const invertChildNode = (node) => {
  if (!node) return node;
  if (!node.left && !node.right) return node;

  invertChildNode(node.left);
  invertChildNode(node.right);

  const temp = node.left;
  node.left = node.right;
  node.right = temp;

  return node;
};

/**
 * @param {TreeNode} root
 * @return {TreeNode}
 */
var invertTree = function (root) {
  if (!root) return root;

  return invertChildNode(root);
};
