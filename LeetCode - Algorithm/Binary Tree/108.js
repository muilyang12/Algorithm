// 108. Convert Sorted Array to Binary Search Tree
// https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

function TreeNode(val, left, right) {
  this.val = val === undefined ? 0 : val;
  this.left = left === undefined ? null : left;
  this.right = right === undefined ? null : right;
}

/**
 * @param {number[]} nums
 * @return {TreeNode}
 */
// time complexity: O(n log n)
// space complexity: O(n)
var sortedArrayToBST = function (nums) {
  if (nums.length === 0) return null;

  const mid = Math.floor(nums.length / 2);

  const newNode = new TreeNode(nums[mid]);
  newNode.left = sortedArrayToBST(nums.slice(0, mid));
  newNode.right = sortedArrayToBST(nums.slice(mid + 1, nums.length));

  return newNode;
};

`
I initially thought the time complexity would be O(n) since each node is visited once, which suggests 
linear time. However, I overlooked the time required to divide the array at each step.

Each split at a certain depth takes O(n) time, and the number of depth is log n. So, the overall complexity
should include an additional n log n. Therefore, the correct time complexity is O(n log n).
`;
