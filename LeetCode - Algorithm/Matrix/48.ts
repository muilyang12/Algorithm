// 48. Rotate Image
// https://leetcode.com/problems/rotate-image/

function rotate(matrix: number[][]): void {
  const l = matrix.length;
  for (let i = 0; i < Math.floor(l / 2); i++) {
    for (let j = 0; j < l - 2 * i - 1; j++) {
      const number1 = matrix[l - 1 - i - j][i];
      const number2 = matrix[i][i + j];
      const number3 = matrix[i + j][l - 1 - i];
      const number4 = matrix[l - 1 - i][l - 1 - i - j];

      matrix[i][i + j] = number1;
      matrix[i + j][l - 1 - i] = number2;
      matrix[l - 1 - i][l - 1 - i - j] = number3;
      matrix[l - 1 - i - j][i] = number4;
    }
  }
}

/*
l = 3

i    j
0 // 1

[1,2,3]
[4,5,6]
[7,8,9]

temp = 3
[1,2,3]
[4,5,6]
[7,8,9]
*/
