// 1679. Max Number of K-Sum Pairs
// https://leetcode.com/problems/max-number-of-k-sum-pairs/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maxOperations = function (nums, k) {
  sortedNums = nums.sort((a, b) => a - b);

  let result = 0;

  let left = 0;
  let right = sortedNums.length - 1;

  while (left < right) {
    if (sortedNums[left] + sortedNums[right] === k) {
      result += 1;

      left += 1;
      right -= 1;
    } else if (sortedNums[left] + sortedNums[right] < k) {
      left += 1;
    } else {
      right -= 1;
    }
  }

  return result;
};
