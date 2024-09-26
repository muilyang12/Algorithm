// 74. Search a 2D Matrix
// https://leetcode.com/problems/search-a-2d-matrix/

/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function (matrix, target) {
  const numRows = matrix.length;
  const numCols = matrix[0].length;

  const numberToCoordinate = (number) => {
    const quotient = Math.floor(number / numCols);
    const remainer = number % numCols;

    return [quotient, remainer];
  };

  let left = 0;
  let right = numRows * numCols - 1;

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);

    const [row, col] = numberToCoordinate(mid);
    const midNumber = matrix[row][col];

    if (midNumber === target) {
      return true;
    } else if (midNumber > target) {
      right = mid - 1;
    } else {
      left = mid + 1;
    }
  }

  return false;
};
