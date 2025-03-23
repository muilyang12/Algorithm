// 62. Unique Paths
// https://leetcode.com/problems/unique-paths/

// time complexity: O(m + n + mn) = O(mn)
// space complexity: O(mn)
class Solution {
    public int uniquePaths(int m, int n) {
        int[][] memo = new int[m][n];

        for (int i = 0; i < m; i++)
            memo[i][n - 1] = 1;
        for (int j = 0; j < n; j++)
            memo[m - 1][j] = 1;

        for (int i = m - 2; i >= 0; i--) {
            for (int j = n - 2; j >= 0; j--) {
                memo[i][j] = memo[i + 1][j] + memo[i][j + 1];
            }
        }

        return memo[0][0];
    }
}

/*
 * m = 3, n = 7
 * 
 * [0,0,0,0,0,0,1]
 * [0,0,0,0,0,0,1]
 * [1,1,1,1,1,1,1]
 */