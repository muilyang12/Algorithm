// 129. Sum Root to Leaf Numbers
// https://leetcode.com/problems/sum-root-to-leaf-numbers/

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

function sumNumbers(root: TreeNode | null): number {
  let result = 0;

  function dfs(node: TreeNode, string: string = "") {
    const newString = string + String(node.val);

    if (!node.left && !node.right) {
      result += Number(newString);

      return;
    }

    if (node.left) dfs(node.left, newString);
    if (node.right) dfs(node.right, newString);
  }

  root && dfs(root);

  return result;
}

`
In this question, I could easily understand that it requires me to use DFS traversal.
`;
