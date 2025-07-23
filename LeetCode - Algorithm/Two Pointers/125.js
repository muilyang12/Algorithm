// 125. Valid Palindrome
// https://leetcode.com/problems/valid-palindrome/

/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {
  const alphabets = "abcdefghijklmnopqrstuvwxyz0123456789";
  const alphabetsSet = new Set(Array.from(alphabets));

  let filteredS = "";

  for (let i = 0; i < s.length; i++) {
    const lower = s[i].toLowerCase();

    if (!alphabetsSet.has(lower)) continue;

    filteredS += lower;
  }

  let left = 0;
  let right = filteredS.length - 1;

  while (left < right) {
    if (filteredS[left] !== filteredS[right]) return false;

    left += 1;
    right -= 1;
  }

  return true;
};

// Please read the question carefully. It literally says "alphanumeric". :(
