// 167. Two Sum II - Input Array Is Sorted
// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (numbers, target) {
  let left = 0;
  let right = numbers.length - 1;

  while (left < right) {
    if (numbers[left] + numbers[right] == target) return [left + 1, right + 1];
    else if (numbers[left] + numbers[right] < target) left += 1;
    else right -= 1;
  }
};

// If I initialize left and right with 0 and 1, it might lead to issues.
