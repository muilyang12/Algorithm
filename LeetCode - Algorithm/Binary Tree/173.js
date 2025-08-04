// 173. Binary Search Tree Iterator
// https://leetcode.com/problems/binary-search-tree-iterator/

function TreeNode(val, left, right) {
  this.val = val === undefined ? 0 : val;
  this.left = left === undefined ? null : left;
  this.right = right === undefined ? null : right;
}

/**
 * @param {TreeNode} root
 */
var BSTIterator = function (root) {
  this.nodes = [];

  getInorder(root, this.nodes);
};

const getInorder = (node, nodes) => {
  if (!node) return;

  getInorder(node.left, nodes);
  nodes.push(node.val);
  getInorder(node.right, nodes);
};

/**
 * @return {number}
 */
BSTIterator.prototype.next = function () {
  return this.nodes.shift();
};

/**
 * @return {boolean}
 */
BSTIterator.prototype.hasNext = function () {
  return this.nodes.length > 0;
};
