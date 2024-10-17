// 48. Rotate Image
// https://leetcode.com/problems/rotate-image/

/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var rotate1 = function (matrix) {
  const numRows = matrix.length;
  const numCols = matrix[0].length;

  // Change matrix dimenstion to square
  if (numRows > numCols) {
    const diff = numRows - numCols;
    const addedZeros = Array(diff).fill(0);

    matrix.forEach((row) => row.push(...addedZeros));
  } else if (numRows < numCols) {
    const diff = numCols - numRows;
    const addedZeros = Array(numCols).fill(0);

    for (let i = 0; i < diff; i++) {
      matrix.push(addedZeros);
    }
  }
  // =========================

  for (let i = 0; i < Math.floor(numRows / 2); i++) {
    const temp = matrix[i];
    matrix[i] = matrix[numRows - 1 - i];
    matrix[numRows - 1 - i] = temp;
  }

  for (let i = 0; i < numRows; i++) {
    for (let j = i + 1; j < numCols; j++) {
      const temp = matrix[i][j];
      matrix[i][j] = matrix[j][i];
      matrix[j][i] = temp;
    }
  }

  // Reset matrix dimension to the original dimension
  if (numRows > numCols) {
    const diff = numRows - numCols;

    for (let i = 0; i < diff; i++) {
      matrix.pop();
    }
  } else if (numRows < numCols) {
    const diff = numCols - numRows;

    matrix.forEach((row) => {
      for (let i = 0; i < diff; i++) {
        row.pop();
      }
    });
  }
  // =========================
};

rotate1([
  [1, 2, 3],
  [4, 5, 6],
]);

`
[4, 1]
[5, 2]
[6, 3]
`;
