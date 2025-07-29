// 383. Ransom Note
// https://leetcode.com/problems/ransom-note/

/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
var canConstruct = function (ransomNote, magazine) {
  const availableLetters = {};

  for (let i = 0; i < magazine.length; i++) {
    if (magazine.charAt(i) in availableLetters) availableLetters[magazine.charAt(i)] += 1;
    else availableLetters[magazine.charAt(i)] = 1;
  }

  for (let i = 0; i < ransomNote.length; i++) {
    if (
      availableLetters[ransomNote.charAt(i)] === undefined ||
      availableLetters[ransomNote.charAt(i)] === 0
    )
      return false;

    availableLetters[ransomNote.charAt(i)] -= 1;
  }

  return true;
};
