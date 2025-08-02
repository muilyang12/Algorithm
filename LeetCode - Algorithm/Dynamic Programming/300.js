// 300. Longest Increasing Subsequence
// https://leetcode.com/problems/longest-increasing-subsequence/

/**
 * @param {number[]} nums
 * @return {number}
 */
var lengthOfLIS = function (nums) {
  let result = 1;

  const memo = [];
  for (let i = 0; i < nums.length; i++) memo.push(1);

  for (let i = 1; i < nums.length; i++) {
    for (let j = 0; j < i; j++) {
      if (nums[i] > nums[j]) {
        memo[i] = Math.max(memo[i], memo[j] + 1);
        result = Math.max(result, memo[i]);
      }
    }
  }

  return result;
};

/*
nums = [10,9,2,5,3,7,101,18]
         ^ ^
*/
