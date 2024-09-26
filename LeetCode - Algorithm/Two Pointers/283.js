// 283. Move Zeroes
// https://leetcode.com/problems/move-zeroes/

/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
// time complexity: O(n)
// space complexity: O(1)
var moveZeroes = function (nums) {
  left = 0;
  right = 1;

  while (left <= right && right < nums.length) {
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

      if (left === right) right += 1;
    } else {
      left += 1;
      right += 1;
    }
  }
};

`
[0,1,0,3,12]
 ^ ^

[4,2,4,0,0,3,0,5,1,0]
 ^ ^

[1,0,2,0,3,12]
 ^ ^
`;
