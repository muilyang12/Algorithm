// 35. Search Insert Position
// https://leetcode.com/problems/search-insert-position/

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */

// Binary Search
// time complexity: O(logn) || space complexity: O(1)
var searchInsert = function (nums, target) {
  let front = 0;
  let rear = nums.length - 1;

  let middle;
  while (front <= rear) {
    middle = Math.floor((front + rear) / 2);
    
    if (nums[middle] < target) {
      front = middle + 1;
    } else if (nums[middle] > target) {
      rear = middle - 1;
    } else {
      return middle;
    }
  }

  return front;
};
