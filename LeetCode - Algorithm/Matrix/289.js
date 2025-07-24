// 289. Game of Life
// https://leetcode.com/problems/game-of-life/

/**
 * @param {number[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
var gameOfLife = function (board) {
  for (let i = 0; i < board.length; i++) {
    for (let j = 0; j < board[0].length; j++) {
      const { numDead, numLive } = getNeighborsStatus(board, i, j);

      if (board[i][j] === 1) {
        if (numLive < 2) board[i][j] = 3;
        else if (numLive > 3) board[i][j] = 3;
      } else if (board[i][j] === 0) {
        if (numLive === 3) board[i][j] = 2;
      }
    }
  }

  for (let i = 0; i < board.length; i++) {
    for (let j = 0; j < board[0].length; j++) {
      if (board[i][j] == 2) board[i][j] = 1;
      else if (board[i][j] == 3) board[i][j] = 0;
    }
  }
};

const getNeighborsStatus = (board, row, col) => {
  const neighbors = [
    [-1, -1],
    [-1, 0],
    [-1, 1],
    [0, -1],
    [0, 1],
    [1, -1],
    [1, 0],
    [1, 1],
  ];

  let numLive = 0;
  let numDead = 0;

  for (const [i, j] of neighbors) {
    if (row + i < 0 || row + i >= board.length) continue;
    if (col + j < 0 || col + j >= board[0].length) continue;

    if (board[row + i][col + j] === 0 || board[row + i][col + j] === 2) numDead += 1;
    else if (board[row + i][col + j] === 1 || board[row + i][col + j] === 3) numLive += 1;
  }

  return { numDead, numLive };
};
