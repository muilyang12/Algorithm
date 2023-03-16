// 617. Merge Two Binary Trees
// https://leetcode.com/problems/merge-two-binary-trees/

/**
 * @param {TreeNode} root1
 * @param {TreeNode} root2
 * @return {TreeNode}
 */

// Depth First Search (DFS)
// time complexity: O(n) (At Best: still O(n)) || space complexity: O(n) (At Best: still O(n))
var mergeTrees1 = function (root1, root2) {
  if (!root1 && !root2) return null;

  let result = new TreeNode();
  let pointer1 = root1;
  let pointer2 = root2;

  dfs(pointer1 ?? new TreeNode(0), pointer2 ?? new TreeNode(0), result);

  return result;
};

const dfs = (root1, root2, result) => {
  result.val = root1.val + root2.val;

  if (root1.left || root2.left) {
    result.left = new TreeNode();

    dfs(
      root1.left ?? new TreeNode(0),
      root2.left ?? new TreeNode(0),
      result.left
    );
  }

  if (root1.right || root2.right) {
    result.right = new TreeNode();

    dfs(
      root1.right ?? new TreeNode(0),
      root2.right ?? new TreeNode(0),
      result.right
    );
  }
};

// Depth First Search (DFS)
// time complexity: O(n) (At Best: O(1)) || space complexity: O(n) (At Best: O(1))
var mergeTrees2 = function (root1, root2) {
  if (!root1 || !root2) return root1 || root2;

  const node = new TreeNode(root1.val + root2.val);

  node.left = mergeTrees2(root1.left, root2.left);
  node.right = mergeTrees2(root1.right, root2.right);

  return node;
};

function TreeNode(val, left, right) {
  this.val = val === undefined ? 0 : val;
  this.left = left === undefined ? null : left;
  this.right = right === undefined ? null : right;
}
