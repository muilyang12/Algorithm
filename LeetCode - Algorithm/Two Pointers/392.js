// 392. Is Subsequence
// https://leetcode.com/problems/is-subsequence/

/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function (nums) {
  left = 0;
  right = 0;

  while (left <= right && right < nums.length) {
    console.log(left, right, nums);

    if (nums[left] === 0 && nums[right] !== 0) {
      temp = nums[left];
      nums[left] = nums[right];
      nums[right] = temp;

      left += 1;
      right += 1;
    } else if (nums[left] === 0 && nums[right] === 0) {
      right += 1;
    } else if (nums[left] !== 0 && nums[right] !== 0) {
      left += 1;
    } else {
      left += 1;
      right += 1;
    }
  }
};
