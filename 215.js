// 215. Kth Largest Element in an Array
// https://leetcode.com/problems/kth-largest-element-in-an-array/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */

// Sort
// time complexity: O(nlogn) || space complexity: O(1)
var findKthLargest1 = function (nums, k) {
  nums.sort((a, b) => {
    if (a > b) return -1;
    else return 1;
  });

  return nums[k - 1];
};

// Min Array
// time complexity: O(nk) || space complexity: O(k)
var findKthLargest2 = function (nums, k) {
  var insertNum = function (array, number) {
    for (let i = 0; i < array.length; i++) {
      if (array[i] <= number) continue;

      const left = array.slice(0, i);
      const right = array.slice(i);

      return [...left, number, ...right];
    }

    return [...array, number];
  };

  let minArray = [];

  for (let i = 0; i < nums.length; i++) {
    minArray = insertNum(minArray, nums[i]);

    if (minArray.length > k) {
      minArray.shift();
    }
  }

  return minArray[0];
};
