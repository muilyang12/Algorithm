// 110. Balanced Binary Tree
// https://leetcode.com/problems/balanced-binary-tree/

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

function isBalanced(root: TreeNode | null): boolean {
  const isCurrentNodeBalanced = Math.abs(getHeight(root?.left) - getHeight(root?.right)) <= 1;
  const isLeftNodeBalanced = root?.left ? isBalanced(root.left) : true;
  const isRightNodeBalanced = root?.right ? isBalanced(root.right) : true;

  return isCurrentNodeBalanced && isLeftNodeBalanced && isRightNodeBalanced;
}

function getHeight(root: TreeNode | null | undefined) {
  if (!root) return 0;

  const leftHeight = getHeight(root?.left) + 1;
  const rightHeight = getHeight(root?.right) + 1;

  return Math.max(leftHeight, rightHeight);
}
