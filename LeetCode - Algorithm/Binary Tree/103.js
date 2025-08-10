// 103. Binary Tree Zigzag Level Order Traversal
// https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

function TreeNode(val, left, right) {
  this.val = val === undefined ? 0 : val;
  this.left = left === undefined ? null : left;
  this.right = right === undefined ? null : right;
}

/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
var zigzagLevelOrder = function (root) {
  const queue = [];
  if (root) queue.push(root);

  const result = [];
  let isRight = true;

  while (queue.length > 0) {
    const currentLength = queue.length;

    const current = [];
    for (let i = 0; i < currentLength; i++) {
      const node = queue.shift();

      if (node.left) queue.push(node.left);
      if (node.right) queue.push(node.right);

      if (isRight) current.push(node.val);
      else current.unshift(node.val);
    }

    result.push(current);

    isRight = !isRight;
  }

  return result;
};
