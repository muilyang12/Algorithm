// 118. Pascal's Triangle
// https://leetcode.com/problems/pascals-triangle/

// Array
function generate(numRows: number): number[][] {
  const result: number[][] = [[1]];

  for (let i = 1; i < numRows; i++) {
    result[i] = [];

    for (let j = 0; j < i + 1; j++) {
      if (j === 0 || j === i) {
        result[i][j] = 1;
      } else {
        result[i][j] = result[i - 1][j - 1] + result[i - 1][j];
      }
    }
  }

  return result;
}
