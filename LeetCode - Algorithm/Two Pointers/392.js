// 392. Is Subsequence
// https://leetcode.com/problems/is-subsequence/

/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isSubsequence = function (s, t) {
  i = 0;
  j = 0;

  while (i < s.length && j < t.length) {
    if (s[i] == t[j]) {
      i += 1;
    }

    j += 1;
  }

  if (i >= s.length) return true;
  else return false;
};
