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
var averageOfLevels1 = function (root) {
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

var averageOfLevels2 = function (root) {
  if (root.length === 0) return [];

  const result = [];

  const queue = [];
  queue.push(root);

  while (queue.length > 0) {
    let sum = 0;
    let count = 0;

    const nodesCount = queue.length;

    for (let i = 0; i < nodesCount; i++) {
      const node = queue.shift();

      sum += node.val;
      count += 1;

      if (node.left) queue.push(node.left);
      if (node.right) queue.push(node.right);
    }

    result.push(sum / count);
  }

  return result;
};

`
Last time, my teammate showed me that I don't need to store the depth information along with the node data if I use 
a for loop inside the while loop. By using only a while loop, I would have had to track the depth manually by 
including it with the node data. However, by including a for loop inside the while loop, I can assume that each 
iteration of the while loop corresponds to moving to the next depth level, and each iteration of the for loop processes
nodes at the same depth.
`;
