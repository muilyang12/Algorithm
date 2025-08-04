// 222. Count Complete Tree Nodes
// https://leetcode.com/problems/count-complete-tree-nodes/

function TreeNode(val, left, right) {
  this.val = val === undefined ? 0 : val;
  this.left = left === undefined ? null : left;
  this.right = right === undefined ? null : right;
}

/**
 * @param {TreeNode} root
 * @return {number}
 */
var countNodes = function (root) {
  let result = 0;

  const queue = [];
  if (root) queue.push(root);

  while (queue.length > 0) {
    const node = queue.shift();
    result += 1;

    if (node.left) queue.push(node.left);
    if (node.right) queue.push(node.right);
  }

  return result;
};
