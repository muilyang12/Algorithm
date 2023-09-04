// 101. Symmetric Tree
// https://leetcode.com/problems/symmetric-tree/

// Tree, Depth First Search (DFS)
// time complexity: O(n)
function isSymmetric(root: TreeNode | null): boolean {
  if (!root) return true;

  return isTwoTreesSame(root.left, root.right);
}

function isTwoTreesSame(leftTreeRoot: TreeNode | null, rightTreeRoot: TreeNode | null) {
  if (!leftTreeRoot && !rightTreeRoot) return true;
  if (!leftTreeRoot || !rightTreeRoot) return false;

  const isCurrentValuesSame = leftTreeRoot.val === rightTreeRoot.val;

  const isOuterTreesSame = isTwoTreesSame(leftTreeRoot.left, rightTreeRoot.right);
  const isInnerTreesSame = isTwoTreesSame(leftTreeRoot.right, rightTreeRoot.left);

  return isCurrentValuesSame && isOuterTreesSame && isInnerTreesSame;
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
