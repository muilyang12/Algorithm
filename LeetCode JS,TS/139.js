// 139. Word Break
// https://leetcode.com/problems/word-break/

/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {boolean}
 */

// Divide-and-conquer
// time complexity: O(2^n) || space complexity: O(n)
// How I can calculate the time complexity: https://stackoverflow.com/questions/31370674/time-complexity-of-the-word-break-recursive-solution
var wordBreak = function (s, wordDict) {
  const wordSet = new Set(wordDict);

  const dfs = function (s) {
    if (s.length === 0) {
      return true;
    }

    let target;
    let tempResult;
    for (let i = 0; i < s.length; i++) {
      target = s.slice(0, i + 1);

      if (!wordSet.has(target)) {
        continue;
      }

      const nextString = s.slice(i + 1);
      tempResult = dfs(nextString);
      if (tempResult) {
        return true;
      }
    }

    return false;
  };

  return dfs(s);
};

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
