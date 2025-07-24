// 219. Contains Duplicate II
// https://leetcode.com/problems/contains-duplicate-ii/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var containsNearbyDuplicate = function (nums, k) {
  const hash = {};

  for (let i = 0; i < nums.length; i++) {
    const num = nums[i];

    if (num in hash) {
      if (i - hash[num][hash[num].length - 1] <= k) return true;

      hash[num].push(i);
    } else {
      hash[num] = [i];
    }
  }

  return false;
};

// If I can recognize that a hashmap is the right approach, it's not that hard. But it's hard to realize that I should use a hashmap in this question.

// Unlike in Python, in JavaScript I have to use arr[arr.length - 1] :(
