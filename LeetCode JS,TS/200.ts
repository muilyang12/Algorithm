// 200. Number of Islands
// https://leetcode.com/problems/number-of-islands/

// Depth First Search (DFS) // Recursive Function
// time complexity: O(2n) = O(n) || space complexity: O(2n) = O(n)
function numIslands1(grid: string[][]): number {
  let result = 0;

  const row = grid.length;
  const col = grid[0].length;
  const checked: boolean[][] = grid.map((row) => row.map(() => false));

  function isAccessible(i: number, j: number) {
    if (i < 0 || i >= row || j < 0 || j >= col) return false;
    if (grid[i][j] === "0") return false;
    if (checked[i][j]) return false;

    return true;
  }

  function fillUpNearArea(i: number, j: number) {
    checked[i][j] = true;

    if (isAccessible(i, j + 1)) fillUpNearArea(i, j + 1);
    if (isAccessible(i + 1, j)) fillUpNearArea(i + 1, j);
    if (isAccessible(i, j - 1)) fillUpNearArea(i, j - 1);
    if (isAccessible(i - 1, j)) fillUpNearArea(i - 1, j);
  }

  for (let i = 0; i < row; i++) {
    for (let j = 0; j < col; j++) {
      if (grid[i][j] === "1" && !checked[i][j]) {
        fillUpNearArea(i, j);
        result += 1;
      }
    }
  }

  return result;
}

// Depth First Search (DFS) // Stack
// time complexity: O(2n) = O(n) || space complexity: O(2n) = O(n)
function numIslands2(grid: string[][]): number {
  let result = 0;

  const numRow = grid.length;
  const numCol = grid[0].length;
  const checked: boolean[][] = grid.map((row) => row.map(() => false));

  function isAccessible(i: number, j: number) {
    if (i < 0 || i >= numRow || j < 0 || j >= numCol) return false;
    if (grid[i][j] === "0") return false;
    if (checked[i][j]) return false;

    return true;
  }

  function fillUpNearArea(i: number, j: number) {
    const stack = [[i, j]];

    while (stack.length > 0) {
      const [i, j] = stack.pop()!;

      checked[i][j] = true;

      if (isAccessible(i, j + 1)) stack.push([i, j + 1]);
      if (isAccessible(i + 1, j)) stack.push([i + 1, j]);
      if (isAccessible(i, j - 1)) stack.push([i, j - 1]);
      if (isAccessible(i - 1, j)) stack.push([i - 1, j]);
    }
  }

  for (let i = 0; i < numRow; i++) {
    for (let j = 0; j < numCol; j++) {
      if (grid[i][j] === "1" && !checked[i][j]) {
        fillUpNearArea(i, j);
        result += 1;
      }
    }
  }

  return result;
}
