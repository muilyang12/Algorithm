// 1143. Longest Common Subsequence
// https://leetcode.com/problems/longest-common-subsequence/

/**
 * @param {string} text1
 * @param {string} text2
 * @return {number}
 */
var longestCommonSubsequence = function (text1, text2) {
  const memo = [];
  for (let i = 0; i < text1.length; i++) {
    memo.push(Array(text2.length).fill(0));
  }

  for (let i = 0; i < text1.length; i++) {
    for (let j = 0; j < text2.length; j++) {
      if (i === 0) {
        if (text1[i] === text2[j] || (j > 0 && memo[i][j - 1] === 1)) memo[i][j] = 1;
      }
      if (j === 0) {
        if (text1[i] === text2[j] || (i > 0 && memo[i - 1][j] === 1)) memo[i][j] = 1;
      }

      if (i > 0 && j > 0) {
        if (text1[i] === text2[j]) memo[i][j] = memo[i - 1][j - 1] + 1;
        else memo[i][j] = Math.max(memo[i - 1][j - 1], memo[i - 1][j], memo[i][j - 1]);
      }
    }
  }

  return memo[text1.length - 1][text2.length - 1];
};

// ext1 = "abcde", text2 = "ace"
// [0,0,0,0,0], [0,0,0]
