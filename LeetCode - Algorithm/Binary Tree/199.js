// 199. Binary Tree Right Side View
// https://leetcode.com/problems/binary-tree-right-side-view/

function TreeNode(val, left, right) {
  this.val = val === undefined ? 0 : val;
  this.left = left === undefined ? null : left;
  this.right = right === undefined ? null : right;
}

/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var rightSideView = function (root) {
  if (!root || root.length === 0) return [];

  const result = [];

  const queue = [];
  queue.push(root);

  while (queue.length > 0) {
    const currentLength = queue.length;

    let node;

    for (let i = 0; i < currentLength; i++) {
      node = queue.shift();

      if (node.left) queue.push(node.left);
      if (node.right) queue.push(node.right);
    }

    result.push(node.val);
  }

  return result;
};
