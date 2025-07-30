// 228. Summary Ranges
// https://leetcode.com/problems/summary-ranges/

/**
 * @param {number[]} nums
 * @return {string[]}
 */
var summaryRanges = function (nums) {
  if (nums.length === 0) return [];

  const result = [];

  let start = 0;
  let end = 0;

  while (end < nums.length) {
    if (nums[end + 1] === nums[end] + 1) {
      end += 1;

      continue;
    }

    if (start === end) {
      result.push(`${nums[start]}`);
    } else {
      result.push(`${nums[start]}->${nums[end]}`);
    }

    start = end + 1;
    end = end + 1;
  }

  return result;
};

/*
nums = [0,2,3,4,6,8,9]
        ^
*/
