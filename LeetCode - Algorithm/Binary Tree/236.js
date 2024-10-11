// 236. Lowest Common Ancestor of a Binary Tree
// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

function TreeNode(val) {
  this.val = val;
  this.left = this.right = null;
}

/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 */
var lowestCommonAncestor = function (root, p, q) {
  if (p.val === q.val) return p.val;

  let pathToP;
  let pathToQ;

  /**
   * @param {TreeNode} node
   */
  const dfs = (node, visited) => {
    if (!node) return;

    visited.push(node);

    if (node.val === p.val) pathToP = [...visited];
    if (node.val === q.val) pathToQ = [...visited];

    dfs(node.left, visited);
    dfs(node.right, visited);

    visited.pop();
  };

  dfs(root, []);

  let current = 0;
  while (current < pathToP.length && current < pathToQ.length) {
    if (pathToP[current].val === pathToQ[current].val) current += 1;
    else break;
  }

  return pathToP[current - 1];
};
