// 118. Pascal's Triangle
// https://leetcode.com/problems/pascals-triangle/

/**
 * @param {number} numRows
 * @return {number[][]}
 */
var generate = function (numRows) {
  const result = [];
  for (let i = 0; i < numRows; i++) {
    const current = Array(i + 1).fill(0);
    current[0] = 1;
    current[i] = 1;

    result.push(current);
  }

  for (let i = 0; i < numRows; i++) {
    for (let j = 1; j < i; j++) {
      result[i][j] = result[i - 1][j - 1] + result[i - 1][j];
    }
  }

  return result;
};
