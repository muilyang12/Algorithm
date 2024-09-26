// 437. Path Sum III
// https://leetcode.com/problems/path-sum-iii/

function TreeNode(val, left, right) {
  this.val = val === undefined ? 0 : val;
  this.left = left === undefined ? null : left;
  this.right = right === undefined ? null : right;
}

/**
 * @param {TreeNode} root
 * @param {number} targetSum
 * @return {number}
 */
var pathSum = function (root, targetSum) {
  let result = 0;

  const getPathCounts = (node, currentSums = [0]) => {
    if (!node) return;

    currentSums.forEach((current) => {
      if (current + node.val === targetSum) result += 1;
    });

    const newCurrentSums = currentSums.map((sum) => sum + node.val);
    newCurrentSums.push(0);

    getPathCounts(node.left, newCurrentSums);
    getPathCounts(node.right, newCurrentSums);
  };

  getPathCounts(root);

  return result;
};

// [[3]]
// [[-2]]
// [[3, 3], [-2, 3]]

`
       10
    5     -3
  3   2     11
3 -2    1
`;

`
10, [0]
5 [10, 0]
3 [15, 5, 0]

-3 [10, 0]
11 [7, -3]
`;
