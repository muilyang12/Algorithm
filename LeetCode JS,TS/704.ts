// 704. Binary Search
// https://leetcode.com/problems/binary-search/

// Divide-and-conquer - Recursive
// time complexity: O(logn) || space complexity: O(1)
function search(nums: number[], target: number): number {
  let left = 0;
  let right = nums.length - 1;

  while (left <= right) {
    let mid = Math.floor((left + right) / 2);

    if (nums[mid] === target) {
      return mid;
    } else if (nums[mid] < target) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }

  return -1;
}
