// 139. Word Break
// https://leetcode.com/problems/word-break/

/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {boolean}
 */
var wordBreak = function (s, wordDict) {
  const memo = [];
  for (let i = 0; i < s.length + 1; i++) memo.push(false);
  memo[0] = true;

  const wordSet = new Set(wordDict);

  for (let i = 0; i < s.length + 1; i++) {
    if (!memo[i]) continue;

    for (let j = i + 1; j < s.length + 1; j++) {
      const targetStr = s.slice(i, j);

      if (wordSet.has(targetStr)) memo[j] = true;
    }
  }

  return memo[s.length];
};

/*
s = "leetcode", wordDict = ["leet","code"]
[1, 0, 0, 0, 0, 0, 0, 1, 0]
                      ^

s = "applepenapple", wordDict = ["apple","pen"]
*/
