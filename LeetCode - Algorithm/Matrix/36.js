// 36. Valid Sudoku
// https://leetcode.com/problems/valid-sudoku/

/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function (board) {
  const boxSetList = [];
  for (let i = 0; i < 9; i++) {
    boxSetList.push(new Set());
  }

  for (let i = 0; i < 9; i++) {
    const rowSet = new Set();
    const colSet = new Set();

    for (let j = 0; j < 9; j++) {
      if (board[i][j] !== "." && rowSet.has(board[i][j])) return false;
      else if (board[i][j] !== "." && !rowSet.has(board[i][j])) rowSet.add(board[i][j]);

      if (board[j][i] !== "." && colSet.has(board[j][i])) return false;
      else if (board[j][i] !== "." && !colSet.has(board[j][i])) colSet.add(board[j][i]);

      const boxSet = boxSetList[3 * Math.floor(i / 3) + Math.floor(j / 3)];

      if (board[i][j] !== "." && boxSet.has(board[i][j])) return false;
      else if (board[i][j] !== "." && !boxSet.has(board[i][j])) boxSet.add(board[i][j]);
    }
  }

  return true;
};
