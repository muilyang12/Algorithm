// 637. Average of Levels in Binary Tree
// https://leetcode.com/problems/average-of-levels-in-binary-tree/

function TreeNode(val, left, right) {
  this.val = val === undefined ? 0 : val;
  this.left = left === undefined ? null : left;
  this.right = right === undefined ? null : right;
}

/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var averageOfLevels = function (root) {
  if (root.length === 0) return [];

  const result = [];
  const counts = [];

  const queue = [];
  queue.push([root, 0]);

  while (queue.length > 0) {
    const [node, depth] = queue.shift();

    if (result[depth] === undefined) {
      result[depth] = 0;
      counts[depth] = 0;
    }

    result[depth] += node.val;
    counts[depth] += 1;

    if (node.left) queue.push([node.left, depth + 1]);
    if (node.right) queue.push([node.right, depth + 1]);
  }

  counts.forEach((count, index) => {
    result[index] /= count;
  });

  return result;
};
