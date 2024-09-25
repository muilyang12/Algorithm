// 73. Set Matrix Zeroes
// https://leetcode.com/problems/set-matrix-zeroes/

/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var setZeroes = function (matrix) {
  const numRows = matrix.length;
  const numCols = matrix[0].length;

  const initialZeros = [];

  for (let i = 0; i < numRows; i++) {
    for (let j = 0; j < numCols; j++) {
      if (matrix[i][j] === 0) initialZeros.push([i, j]);
    }
  }

  initialZeros.forEach(([xCoordinate, yCoordinate]) => {
    for (let i = 0; i < numRows; i++) {
      matrix[i][yCoordinate] = 0;
    }

    for (let i = 0; i < numCols; i++) {
      matrix[xCoordinate][i] = 0;
    }
  });
};
