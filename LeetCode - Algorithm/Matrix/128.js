// 128. Longest Consecutive Sequence
// https://leetcode.com/problems/longest-consecutive-sequence/

/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function (nums) {
  const numsSet = new Set(nums);

  const targets = [];

  for (let i = 0; i < nums.length; i++) {
    if (numsSet.has(nums[i] + 1)) continue;

    targets.push(nums[i]);
  }

  let result = 0;
  for (let i = 0; i < targets.length; i++) {
    let currentResult = 0;
    let numToCheck = targets[i];
    while (numsSet.has(numToCheck)) {
      currentResult += 1;
      numToCheck -= 1;
    }

    result = Math.max(result, currentResult);
  }

  return result;
};

// I should remember that I can't select a number from a set using indexing.
// And, it's annoying that same logic passed in Python but failed in JS. :(

/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function (nums) {
  const numsSet = new Set(nums);

  let result = 0;
  for (let i = 0; i < nums.length; i++) {
    if (numsSet.has(nums[i] + 1)) continue;

    let currentResult = 0;
    let currentTarget = nums[i];
    while (numsSet.has(currentTarget)) {
      currentResult += 1;
      currentTarget -= 1;
    }

    result = Math.max(result, currentResult);
  }

  return result;
};

/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function (nums) {
  const numsSet = new Set(nums);

  let result = 0;
  for (let i = 0; i < nums.length; i++) {
    if (numsSet.has(nums[i] + 1)) continue;

    let length = 1;
    while (numsSet.has(nums[i] - length)) {
      length += 1;
    }

    result = Math.max(result, length);
  }

  return result;
};

/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function (nums) {
  const numsSet = new Set(nums);

  let result = 0;
  for (let i = 0; i < nums.length; i++) {
    if (numsSet.has(nums[i] - 1)) continue;

    let length = 1;
    while (numsSet.has(nums[i] + length)) {
      length += 1;
    }

    result = Math.max(result, length);
  }

  return result;
};

/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function (nums) {
  const numsSet = new Set(nums);

  let result = 0;
  for (let num of nums) {
    if (numsSet.has(num - 1)) continue;

    let length = 1;
    while (numsSet.has(num + length)) {
      length += 1;
    }

    result = Math.max(result, length);
  }

  return result;
};
