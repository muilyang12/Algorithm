// 100. Same Tree
// https://leetcode.com/problems/same-tree/

// Breadth First Search (BFS) // Queue
// time complexity: O(n) || space complexity: O(n)
function isSameTree1(p: TreeNode | null, q: TreeNode | null): boolean {
  if (!p && !q) return true;
  if (!p || !q) return false;

  const queue: [TreeNode, TreeNode][] = [];
  queue.push([p, q]);

  while (queue.length > 0) {
    const [pp, qq] = queue.shift() as [TreeNode, TreeNode];

    if (pp.val !== qq.val) return false;

    if (pp.left && qq.left) {
      queue.push([pp.left, qq.left]);
    } else if (!pp.left && !qq.left) {
    } else {
      return false;
    }
    if (pp.right && qq.right) {
      queue.push([pp.right, qq.right]);
    } else if (!pp.right && !qq.right) {
    } else {
      return false;
    }
  }

  return true;
}

class TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;

  constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
  }
}
