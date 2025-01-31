// 200. Number of Islands
// https://leetcode.com/problems/number-of-islands/

class Solution {
    public int numIslands(char[][] grid) {
        int numRows = grid.length;
        int numCols = grid[0].length;

        boolean[][] visited = new boolean[numRows][numCols];

        int result = 0;

        for (int i = 0; i < numRows; i++) {
            for (int j = 0; j < numCols; j++) {
                if (visited[i][j]) {
                    continue;
                }

                if (grid[i][j] == '0') {
                    visited[i][j] = true;

                    continue;
                }

                dfs(i, j, grid, visited);

                result += 1;
            }
        }

        return result;
    }

    public void dfs(int row, int col, char[][] grid, boolean[][] visited) {
        int numRows = grid.length;
        int numCols = grid[0].length;

        if (row < 0 || row >= numRows) {
            return;
        } else if (col < 0 || col >= numCols) {
            return;
        }

        if (visited[row][col]) {
            return;
        }

        if (grid[row][col] == '0') {
            return;
        }

        visited[row][col] = true;

        int[][] dxdys = {
                { 1, 0 },
                { -1, 0 },
                { 0, 1 },
                { 0, -1 }
        };

        for (int[] dxdy : dxdys) {
            int dx = dxdy[0];
            int dy = dxdy[1];

            dfs(row + dx, col + dy, grid, visited);
        }
    }
}
