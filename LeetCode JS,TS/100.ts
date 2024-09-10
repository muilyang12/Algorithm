// 100. Same Tree
// https://leetcode.com/problems/same-tree/

// Breadth First Search (BFS) // Queue
// time complexity: O(n) || space complexity: O(n)
function isSameTree1(p: TreeNode | null, q: TreeNode | null): boolean {
  const queue: [TreeNode | null, TreeNode | null][] = [];
  queue.push([p, q]);

  while (queue.length > 0) {
    const [pp, qq] = queue.shift() as [TreeNode | null, TreeNode | null];
    if (!pp && !qq) continue;
    if (!pp || !qq) return false;
    if (pp.val !== qq.val) return false;

    queue.push([pp.left, qq.left]);
    queue.push([pp.right, qq.right]);
  }

  return true;
}

// Depth First Search (DFS) // Stack
// time complexity: O(n) || space complexity: O(n)
function isSameTree2(p: TreeNode | null, q: TreeNode | null): boolean {
  const stack: [TreeNode | null, TreeNode | null][] = [];
  stack.push([p, q]);

  while (stack.length > 0) {
    const [pp, qq] = stack.pop() as [TreeNode | null, TreeNode | null];
    if (!pp && !qq) continue;
    if (!pp || !qq) return false;
    if (pp.val !== qq.val) return false;

    stack.push([pp.left, qq.left]);
    stack.push([pp.right, qq.right]);
  }

  return true;
}

// Depth First Search (DFS) // Recursive Function
// time complexity: O(n) || space complexity: O(n)
function isSameTree3(p: TreeNode | null, q: TreeNode | null): boolean {
  if (!p && !q) return true;
  if (!p || !q) return false;
  if (p.val != q.val) return false;

  return isSameTree3(p.left, q.left) && isSameTree3(p.right, q.right);
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
