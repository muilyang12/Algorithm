// 54. Spiral Matrix
// https://leetcode.com/problems/spiral-matrix/

/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function (matrix) {
  const m = matrix.length;
  const n = matrix[0].length;

  const result = [];

  while (matrix.length > 0 && matrix[0].length > 0) {
    result.push(...matrix.shift());

    if (matrix.length === 0 || matrix[0].length === 0) break;

    for (let i = 0; i < matrix.length; i++) {
      result.push(matrix[i].pop());
    }

    if (matrix.length === 0 || matrix[0].length === 0) break;

    result.push(...matrix.pop().reverse());

    if (matrix.length === 0 || matrix[0].length === 0) break;

    for (let i = matrix.length - 1; i >= 0; i--) {
      result.push(matrix[i].shift());
    }
  }

  return result;
};
