// 114. Flatten Binary Tree to Linked List
// https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

function TreeNode(val, left, right) {
  this.val = val === undefined ? 0 : val;
  this.left = left === undefined ? null : left;
  this.right = right === undefined ? null : right;
}

/**
 * @param {TreeNode} root
 * @return {void} Do not return anything, modify root in-place instead.
 */
var flatten = function (root) {
  getEnd(root);
};

const getEnd = (node) => {
  if (!node) return;

  if (node.left && node.right) {
    const leftEnd = getEnd(node.left);
    const rightEnd = getEnd(node.right);

    const temp = node.right;
    node.right = node.left;
    node.left = null;
    leftEnd.right = temp;

    return rightEnd;
  } else if (!node.left && node.right) {
    const rightEnd = getEnd(node.right);

    return rightEnd;
  } else if (node.left && !node.right) {
    const leftEnd = getEnd(node.left);

    node.right = node.left;
    node.left = null;

    return leftEnd;
  } else {
    return node;
  }
};
