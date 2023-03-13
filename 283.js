// 283. Move Zeroes
// https://leetcode.com/problems/move-zeroes/

/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */

// Brute Force
// time complexity: O(n^2) || space complexity: O(1)
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

// Array
// time complexity: O(2n) = O(n) || space complexity: O(n)
var moveZeroes2 = function (nums) {
  const zeroArray = [];
  const nonZeroArray = [];

  for (let i = 0; i < nums.length; i++) {
    if (nums[i] === 0) zeroArray.push(nums[i]);
    else nonZeroArray.push(nums[i]);
  }

  let index = 0;

  nonZeroArray.forEach((num) => {
    nums[index] = num;

    index += 1;
  });

  zeroArray.forEach(num => {
    nums[index] = 0;

    index += 1;
  });
}

// Two Pointer
// time complexity: O(n) || space complexity: O(1)
var moveZeroes3 = function (nums) {
  let targetIndex = -1;

  for (let i = 0; i < nums.length; i++) {
    if (targetIndex < 0 && nums[i] === 0) {
      targetIndex = i;
    }

    if (targetIndex >= 0 && nums[i] !== 0) {
      let temp = nums[targetIndex];

      nums[targetIndex] = nums[i];
      nums[i] = temp;

      targetIndex = targetIndex + 1;
    }
  }
};
