// 283. Move Zeroes
// https://leetcode.com/problems/move-zeroes/

// Brute Force
// time complexity: O(n^2) || space complexity: O(1)
/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes1 = function (nums) {
  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[i] !== 0) break;

      if (nums[j] !== 0) {
        let temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;

        break;
      }
    }
  }
};
