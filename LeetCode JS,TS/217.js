// 217. Contains Duplicate
// https://leetcode.com/problems/contains-duplicate/

/**
 * @param {number[]} nums
 * @return {boolean}
 */

// Brute Force
// time complexity: O(n^2) || space complexity: O(1)
var containsDuplicate1 = function (nums) {
  const length = nums.length;

  for (let i = 0; i < length; i++) {
    for (let j = i + 1; j < length; j++) {
      if (nums[i] === nums[j]) return true;
    }
  }

  return false;
};

// Hash Table
// time complexity: O(n) || space complexity: O(n)
var containsDuplicate2 = function (nums) {
  const hastTable = new Map();

  const length = nums.length;
  for (let i = 0; i < length; i++) {
    if (hastTable.has(nums[i])) return true;

    hastTable.set(nums[i], true);
  }

  return false;
};

// Set
// time complexity: O(n) || space complexity: O(n)
var containsDuplicate3 = function (nums) {
  const set = new Set(nums);

  if (nums.length !== set.size) return true;
  else return false;
};
