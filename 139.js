// 139. Word Break
// https://leetcode.com/problems/word-break/

/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {boolean}
 */

// Divide-and-conquer
var wordBreak = function (s, wordDict) {};

// Dynamic Programming
// time complexity: O(w + n^2 * w) = O(n^2 * w) || space complexity: O(n)
var wordBreak = function (s, wordDict) {
  const wordSet = new Set(wordDict);

  const length = s.length;

  const memo = new Array(length + 1).fill(false);
  memo[0] = true;

  let target;
  for (let i = 0; i < length; i++) {
    for (let j = i; j < length; j++) {
      target = s.slice(i, j + 1);

      if (wordSet.has(target) && memo[i]) {
        memo[j + 1] = memo[i];
      }
    }
  }

  return memo[length];
};
