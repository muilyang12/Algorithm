// 226. Invert Binary Tree
// https://leetcode.com/problems/invert-binary-tree/

// Divide-and-conquer
// time complexity: O(n) || space complexity: O(n) => Depth of stack
function invertTree1(root: TreeNode | null): TreeNode | null {
  if (root === null) return root;
  if (root.left === null && root.right === null) return root;

  const temp = root.left;
  root.left = root.right;
  root.right = temp;

  invertTree1(root.left);
  invertTree1(root.right);

  return root;
}

// Depth First Search (DFS) // Stack
// time complexity: O(n) || space complexity: O(n)
function invertTree2(root: TreeNode | null): TreeNode | null {
  if (root === null) return root;

  const stack: TreeNode[] = [];
  stack.push(root);

  while (stack.length > 0) {
    const node = stack.pop();

    if (!node) break;

    const temp = node.left;
    node.left = node.right;
    node.right = temp;

    if (node.left) stack.push(node.left);
    if (node.right) stack.push(node.right);
  }

  return root;
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
