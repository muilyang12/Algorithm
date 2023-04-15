/**
 * @param {string} s
 * @return {string}
 */

// time complexity: O(n * 2n) = O(n^2) || space complexity: O(1)
var longestPalindrome = function (s) {
  let longestStringLength = 0;
  let result = "";

  for (let i = 0; i < s.length; i++) {
    for (let j = 0; j < s.length; j++) {
      let left = i - j;
      let right = i + j;

      if (left < 0 && right > s.length - 1) break;
      if (s[left] !== s[right]) break;

      if (right - left + 1 > longestStringLength) {
        longestStringLength = right - left + 1;
        result = s.slice(left, right + 1);
      }
    }

    for (let j = 0; j < s.length; j++) {
      let left = i - j;
      let right = i + 1 + j;

      if (left < 0 && right > s.length - 1) break;
      if (s[left] !== s[right]) break;

      if (right - left + 1 > longestStringLength) {
        longestStringLength = right - left + 1;
        result = s.slice(left, right + 1);
      }
    }
  }

  return result;
};
