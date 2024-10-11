// 36. Valid Sudoku
// https://leetcode.com/problems/valid-sudoku/

function isValidSudoku(board: string[][]): boolean {
  const length = 9;

  for (let i = 0; i < length; i++) {
    const checkRowSet = new Set();
    const checkColSet = new Set();

    for (let j = 0; j < length; j++) {
      const valueCheckRow = board[i][j];

      if (valueCheckRow !== "." && checkRowSet.has(valueCheckRow)) return false;
      else if (valueCheckRow !== ".") checkRowSet.add(valueCheckRow);

      const valueCheckCol = board[j][i];

      if (valueCheckCol !== "." && checkColSet.has(valueCheckCol)) return false;
      else if (valueCheckCol !== ".") checkColSet.add(valueCheckCol);
    }
  }

  for (let i = 0; i < length; i++) {
    const checkBlockSet = new Set();

    const blockRow = Math.floor(i / 3);
    const blockCol = i % 3;

    for (let j = 0; j < length / 3; j++) {
      for (let k = 0; k < length / 3; k++) {
        const valueCheckBlock = board[3 * blockRow + j][3 * blockCol + k];

        if (valueCheckBlock !== "." && checkBlockSet.has(valueCheckBlock)) return false;
        else if (valueCheckBlock !== ".") checkBlockSet.add(valueCheckBlock);
      }
    }
  }

  return true;
}

`
It is a very simple question. I can check the row, column, and block in that order.
`;
