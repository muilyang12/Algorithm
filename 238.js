// 238. Product of Array Except Self
// https://leetcode.com/problems/product-of-array-except-self/

/**
 * @param {number[]} nums
 * @return {number[]}
 */

// Brute Force
// time complexity: O(n^2) || space complexity: O(1)
var productExceptSelf1 = function (nums) {
  const result = [];

  for (let i = 0; i < nums.length; i++) {
    let left = 1;
    for (let j = i - 1; j >= 0; j--) {
      left *= nums[j];
    }

    let right = 1;
    for (let j = i + 1; j < nums.length; j++) {
      right *= nums[j];
    }

    result[i] = left * right;
  }

  return result;
};

// Dynamic Programming
// time complexity: O(2n) = O(n) || space complexity: O(2n) = O(n)
var productExceptSelf2 = function (nums) {
  const left = [];
  const right = [];
  let j;
  for (let i = 0; i < nums.length; i++) {
    j = nums.length - 1 - i;
    if (i === 0) {
      left[i] = 1;
      right[j] = 1;

      continue;
    }

    left[i] = left[i - 1] * nums[i - 1];
    right[j] = right[j + 1] * nums[j + 1];
  }

  const result = [];
  for (let i = 0; i < nums.length; i++) {
    result[i] = left[i] * right[i];
  }

  return result;
};
